---
layout: post
title: "各种TimeStamp"
date: 2007-05-31
tags: [技术]
categories: [技术]
---

关于各种Timestamps的区别和比较：

<style type="text/css">.title { color: #00f }</style>


<span class="title">UNIX timestamp</span>: seconds since midnight, January 1, 1970 UTC. It is a 32-bit number.

<span class="title">Win32 FILETIME</span> values count 100-nanosecond intervals since January 1, 1600 UTC. It is a 64-bit number.

<span class="title">CLR System.DateTime</span> values count 100-nanosecond intervals since January 1, 1 UTC. It is a 64-bit number. These aren\'t used much yet.

<span class="title">The DOS date/time</span> format is a bitmask (YYYYYYYM MMMDDDDD hhhhhmmm mmmsssss) The year is stored as an offset from 1980. Seconds are stored in two-second increments. These values are recorded in local time.

<span class="title">The OLE automation date (DATE)</span> format is a floating point value, counting days since midnight 30 December 1899. Hours and minutes are represented as fractional days.

<span class="title">The C runtime time_t</span> value is the same as a UNIX timestamp, 

<span class="title">__time64_t</span> is same except using 64-bit number

* time_t: 19:14:07, January 18, 2038, UTC.
* __time64_t: 23:59:59, December 31, 3000, UTC.

```
struct tm {    
    int tm_sec;     /* seconds after the minute - [0,59] */    
    int tm_min;     /* minutes after the hour - [0,59] */    
    int tm_hour;    /* hours since midnight - [0,23] */    
    int tm_mday;    /* day of the month - [1,31] */    
    int tm_mon;     /* months since January - [0,11] */    
    int tm_year;    /* years since 1900 */    
    int tm_wday;    /* days since Sunday - [0,6] */    
    int tm_yday;    /* days since January 1 - [0,365] */    
    int tm_isdst;   /* daylight savings time flag */    
};

typedef struct _SYSTEMTIME {
    WORD wYear;         /* no offset */
    WORD wMonth;        /* January is 1 */
    WORD wDayOfWeek;    /* Sunday is 0, Monday is 1, and so on.*/
    WORD wDay;          /* 1-31 */
    WORD wHour;
    WORD wMinute;
    WORD wSecond;
    WORD wMilliseconds;
} SYSTEMTIME, *PSYSTEMTIME, *LPSYSTEMTIME;
```

<span class="title">CTime</span> 构造函数可以接受：

```
__time64_t(time_t),
{
    DosDate, 
    DosTime
},
SYSTEMTIME,FILETIME,
{
    nYear: 1970-3000, 
    nMonth: 1-12, 
    nDay: 1-31, 
    nHour, 
    nMin, 
    nSec
}.

struct tm* GetGmtTm(struct tm* ptm = NULL) const;
struct tm* GetLocalTm(struct tm* ptm = NULL) const;
BOOL GetAsSystemTime(SYSTEMTIME& timeDest) const;
time_t GetTime() const;
int GetYear() const;
int GetMonth() const;       // month of year (1 = Jan)
int GetDay() const;         // day of month
int GetHour() const;
int GetMinute() const;
int GetSecond() const;
int GetDayOfWeek() const;   // 1=Sun, 2=Mon, ..., 7=Sat
```

<span class="title">COleDateTime</span> 构造函数可以接收：

```
VARIANT,DATE,time_t,SYSTEMTIME,FILETIME,
{
    nYear: 100-9999, 
    month: 0-12(from 1), 
    day: 0-31 (from 1), 
    hour: 0-23, 
    minute: 0-59, 
    second 0-59
}

BOOL GetAsSystemTime(SYSTEMTIME& sysTime) const;
int GetYear() const;
int GetMonth() const;       // month of year (1 = Jan)
int GetDay() const;         // day of month (0-31)
int GetHour() const;        // hour in day (0-23)
int GetMinute() const;      // minute in hour (0-59)
int GetSecond() const;      // second in minute (0-59)
int GetDayOfWeek() const;   // 1=Sun, 2=Mon, ..., 7=Sat
int GetDayOfYear() const;   // days since start of year, Jan 1 = 1
```

[http://www.codeproject.com/datetime/datetimedisc.asp](http://www.codeproject.com/datetime/datetimedisc.asp)

[http://blogs.msdn.com/oldnewthing/archive/2003/09/05/54806.aspx](http://blogs.msdn.com/oldnewthing/archive/2003/09/05/54806.aspx)
