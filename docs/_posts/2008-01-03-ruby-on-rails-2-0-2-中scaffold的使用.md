---
layout: post
title: "Ruby on Rails 2.0.2 中scaffold的使用"
date: 2008-01-03
tags: [技术]
categories: [技术]
---

照着《Web开发敏捷之道》，写里面的depot例子，一开始就遭遇挫折：

```ruby
class AdminControll < ApplicationController
  scaffold :product
end
```

加了 `scaffold :product` 之后，运行提示：`undefined method 'scaffold' for ActionController:Class.`

直接用后面的 `depot>ruby script/generate scaffold product admin` 也不管用。

上网查了查，应该是 2.0.2 中不再这样支持了，要用下面的语法：

```bash
ruby script/generate scaffold product title:string description:text image_url:string
```

注意，网上有的地方是写 `ruby script/generate scaffold ModelName [field:type, field:type]` 但实际上不能写 `[]`，也不能写 `,`，在这上面折腾了比较长时间。最后还是通过直接运行 `ruby script/generate scaffold` 看它的帮助和示例才明白过来。

这样生成的 `001_create_products.rb` 里面也自动定义了相关的字段，不用手工添加了。自动生成的和书上例子里面也稍有不同，书中例子是：

```ruby
class CreateProducts < ActiveRecord::Migration
  def self.up
    create_table :products do |t|
      t.column :title, :string
      t.column :description, :text
      t.column :image_url, :string
      t.timestamps
    end
  end

  def self.down
    drop_table :products
  end
end
```

自动生成的是：

```ruby
class CreateProducts < ActiveRecord::Migration
  def self.up
    create_table :products do |t|
      t.string :title
      t.text :description
      t.string :image_url
      t.timestamps
    end
  end

  def self.down
    drop_table :products
  end
end
```
