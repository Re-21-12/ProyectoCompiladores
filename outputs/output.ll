; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"a" = alloca i32
  store i32 3, i32* %"a"
  %"b" = alloca i32
  store i32 1, i32* %"b"
  %"c" = alloca i32
  store i32 2, i32* %"c"
  %"a.val" = load i32, i32* %"a"
  %"b.val" = load i32, i32* %"b"
  %"c.val" = load i32, i32* %"c"
  %".5" = call i32 @"selectionSort"(i32 %"a.val", i32 %"b.val", i32 %"c.val")
  ret i32 0
}

define i32 @"selectionSort"(i32 %".1", i32 %".2", i32 %".3")
{
entry:
  %"x.addr" = alloca i32
  store i32 %".1", i32* %"x.addr"
  %"y.addr" = alloca i32
  store i32 %".2", i32* %"y.addr"
  %"z.addr" = alloca i32
  store i32 %".3", i32* %"z.addr"
  %"y.val" = load i32, i32* %"y.addr"
  %"x.val" = load i32, i32* %"x.addr"
  %".8" = icmp slt i32 %"y.val", %"x.val"
  br i1 %".8", label %"if.then0", label %"if.else0"
if.end:
  ret i32 0
if.then0:
  %"tmp" = alloca i32
  %"x.val.1" = load i32, i32* %"x.addr"
  store i32 %"x.val.1", i32* %"tmp"
  %"y.val.1" = load i32, i32* %"y.addr"
  store i32 %"y.val.1", i32* %"x.addr"
  %"tmp.val" = load i32, i32* %"tmp"
  store i32 %"tmp.val", i32* %"y.addr"
  br label %"if.end"
if.else0:
  %"z.val" = load i32, i32* %"z.addr"
  %"x.val.2" = load i32, i32* %"x.addr"
  %".14" = icmp slt i32 %"z.val", %"x.val.2"
  br i1 %".14", label %"if.then1", label %"if.else1"
if.then1:
  %"tmp.1" = alloca i32
  %"x.val.3" = load i32, i32* %"x.addr"
  store i32 %"x.val.3", i32* %"tmp.1"
  %"z.val.1" = load i32, i32* %"z.addr"
  store i32 %"z.val.1", i32* %"x.addr"
  %"tmp.val.1" = load i32, i32* %"tmp.1"
  store i32 %"tmp.val.1", i32* %"z.addr"
  br label %"if.end"
if.else1:
  %"tmp.2" = alloca i32
  %"y.val.2" = load i32, i32* %"y.addr"
  store i32 %"y.val.2", i32* %"tmp.2"
  %"z.val.2" = load i32, i32* %"z.addr"
  store i32 %"z.val.2", i32* %"y.addr"
  %"tmp.val.2" = load i32, i32* %"tmp.2"
  store i32 %"tmp.val.2", i32* %"z.addr"
  br label %"if.end"
}
