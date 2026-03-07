#!/usr/bin/env python3
"""
抓取动态渲染的网页内容
使用 Playwright 控制浏览器获取 JavaScript 渲染后的内容
"""

import asyncio
import sys
import argparse
from playwright.async_api import async_playwright


async def fetch_article(url: str, wait_selector: str = None, timeout: int = 10000):
    """
    抓取动态渲染的网页

    Args:
        url: 目标URL
        wait_selector: 等待某个选择器出现后再提取内容（可选）
        timeout: 超时时间（毫秒）

    Returns:
        (title, content, publish_time): 标题、内容、发布时间（可能为 None）
    """
    async with async_playwright() as p:
        # 启动浏览器（使用 Chromium）
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print(f"正在访问: {url}")

        try:
            # 访问页面
            await page.goto(url, timeout=timeout, wait_until="networkidle")

            # 如果指定了等待选择器，等待其出现
            if wait_selector:
                print(f"等待选择器: {wait_selector}")
                await page.wait_for_selector(wait_selector, timeout=timeout)

            # 额外等待确保内容加载完成
            await asyncio.sleep(2)

            # 提取发布时间 - 尝试多种选择器
            publish_time = None
            import re

            # 先从页面文本中提取标准格式的日期
            page_text = await page.inner_text("body")
            date_match = re.search(r'(\d{4})-(\d{1,2})-(\d{1,2})\s+\d{1,2}:\d{1,2}', page_text)
            if date_match:
                year, month, day = date_match.groups()
                publish_time = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                print(f"从页面文本找到发布时间: {publish_time}")

            # 如果没找到，尝试从元素中提取
            if not publish_time:
                time_selectors = [
                    "time",
                    "[class*='time']",
                    "[class*='date']",
                    ".article-sub-info",
                    ".article-info",
                    "span[class*='time']",
                ]

                for selector in time_selectors:
                    try:
                        element = await page.query_selector(selector)
                        if element:
                            time_text = await element.inner_text()
                            # 尝试中文日期格式: 2024年04月22日
                            cn_date_match = re.search(r'(\d{4})年(\d{1,2})月(\d{1,2})日', time_text)
                            if cn_date_match:
                                year, month, day = cn_date_match.groups()
                                publish_time = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                                print(f"找到发布时间: {publish_time}")
                                break
                            # 尝试标准日期格式
                            date_match = re.search(r'(\d{4})-(\d{1,2})-(\d{1,2})', time_text)
                            if date_match:
                                year, month, day = date_match.groups()
                                publish_time = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                                print(f"找到发布时间: {publish_time}")
                                break
                    except:
                        continue

            # 提取文章内容（通用选择器）
            # 尝试多种可能的文章内容选择器
            content = None
            selectors = [
                "article",
                ".article-content",
                ".article-content__content",
                "[class*='article']",
                "[class*='content']",
                "main",
            ]

            for selector in selectors:
                try:
                    element = await page.query_selector(selector)
                    if element:
                        content = await element.inner_text()
                        if len(content) > 100:  # 确保内容足够长
                            break
                except:
                    continue

            # 如果上述选择器都没找到，获取整个 body
            if not content or len(content) < 100:
                content = await page.inner_text("body")

            # 提取标题
            title = await page.title()

            return title, content, publish_time

        finally:
            await browser.close()


def format_as_markdown(title: str, content: str, url: str, publish_time: str = None) -> tuple:
    """
    将内容格式化为 Markdown 博客格式

    Args:
        title: 文章标题
        content: 文章内容
        url: 原始URL
        publish_time: 发布时间（可选）

    Returns:
        (filename, markdown): 文件名和 Markdown 内容
    """
    import re

    # 清理标题 - 去掉" - 今日头条"等后缀
    clean_title = re.sub(r'\s*[-–—]\s*(今日头条|Toutiao).*$', '', title).strip()

    # 使用发布时间，如果没有则从标题中提取，或使用当前日期
    if publish_time:
        date_str = publish_time
    else:
        date_match = re.search(r'(\d{4})-(\d{1,2})-(\d{1,2})', title)
        if date_match:
            year, month, day = date_match.groups()
            date_str = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        else:
            from datetime import datetime
            date_str = datetime.now().strftime("%Y-%m-%d")

    # 检测是否为 Mojo 相关文章
    combined_text = (title + " " + content).lower()
    is_mojo = 'mojo' in combined_text

    # 生成标签
    tags = ['技术']
    if is_mojo:
        tags.append('Mojo')

    # 从清理后的标题生成文件名（限制长度避免超出系统限制）
    filename = re.sub(r'[^\w\u4e00-\u9fff]+', '-', clean_title).strip('-')
    # 限制标题部分长度（约50个字符）
    if len(filename) > 50:
        filename = filename[:50].rstrip('-')
    filename = f"{date_str}-{filename}.md"

    tags_str = ', '.join(tags)

    markdown = f"""---
layout: post
title: "{clean_title}"
date: {date_str}
tags: [{tags_str}]
categories: [技术]
original_url: {url}
---

{content}
"""
    return filename, markdown


async def main():
    parser = argparse.ArgumentParser(description="抓取动态渲染的网页内容")
    parser.add_argument("url", help="目标URL")
    parser.add_argument("-o", "--output", help="输出文件路径")
    parser.add_argument("-w", "--wait", help="等待的选择器")
    parser.add_argument("--headless", action="store_true", default=True, help="无头模式")

    args = parser.parse_args()

    try:
        title, content, publish_time = await fetch_article(args.url, args.wait)

        print(f"\n标题: {title}")
        if publish_time:
            print(f"发布时间: {publish_time}")
        print(f"\n内容预览:")
        print(content[:500] + "..." if len(content) > 500 else content)

        filename, markdown = format_as_markdown(title, content, args.url, publish_time)

        if args.output:
            filename = args.output

        # 保存到文件
        output_path = f"_posts/{filename}" if '/' not in filename else filename
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"\n已保存到: {output_path}")

    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
