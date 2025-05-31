; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %"for.cond"
for.cond:
  %"i.val" = load i32, i32* %"i"
  %"i.val.1" = load i32, i32* %"i"
  %"cmptmp" = icmp slt i32 %"i.val.1", 100000
  br i1 %"cmptmp", label %"for.body", label %"for.end"
for.body:
  %"i.val.2" = load i32, i32* %"i"
  %".5" = bitcast [8 x i8]* @"fmt_0" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %"i.val.2")
  br label %"for.update"
for.update:
  %"i.val.3" = load i32, i32* %"i"
  %".8" = load i32, i32* %"i"
  %".9" = add i32 %".8", 1
  store i32 %".9", i32* %"i"
  br label %"for.cond"
for.end:
  ret i32 0
}

@"fmt_0" = internal constant [8 x i8] c"%d\5c0a\5c00"