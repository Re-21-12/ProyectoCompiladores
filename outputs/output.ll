; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  %"limite" = alloca i32
  store i32 10, i32* %"limite"
  br label %"while.cond"
while.cond:
  %"i.val" = load i32, i32* %"i"
  %"limite.val" = load i32, i32* %"limite"
  %"cmptmp" = icmp slt i32 %"i.val", %"limite.val"
  br i1 %"cmptmp", label %"while.body", label %"while.end"
while.body:
  %"i.val.1" = load i32, i32* %"i"
  %"call_fibonacci" = call i32 @"fibonacci"(i32 %"i.val.1")
  %".6" = bitcast [4 x i8]* @"fmt.0" to i8*
  %".7" = call i32 (i8*, ...) @"printf"(i8* %".6", i32 %"call_fibonacci")
  %"i.val.2" = load i32, i32* %"i"
  store i32 %"i.val.2", i32* %"i"
  br label %"while.cond"
while.end:
  ret i32 0
}

define i32 @"fibonacci"(i32 %".1")
{
entry:
  %"n.addr" = alloca i32
  store i32 %".1", i32* %"n.addr"
  %".4" = icmp ne i32 0, 0
  br i1 %".4", label %"if.then", label %"if.else"
if.then:
  br label %"if.end"
if.end:
  ret i32 0
if.else:
  %"n.val" = load i32, i32* %"n.addr"
  %"call_fibonacci" = call i32 @"fibonacci"(i32 %"n.val")
  ret i32 %"call_fibonacci"
}

@"fmt.0" = internal constant [4 x i8] c"%d\0a\00"