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
  %"cmptmp" = icmp slt i32 %"i.val", 10
  br i1 %"cmptmp", label %"for.body", label %"for.end"
for.body:
  %"i.val.1" = load i32, i32* %"i"
  %".5" = bitcast [4 x i8]* @"fmt.0" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", i32 %"i.val.1")
  br label %"for.update"
for.update:
  br label %"for.cond"
for.end:
  ret i32 0
}

@"fmt.0" = internal constant [4 x i8] c"%d\0a\00"