; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 5, i32* %"x"
  %"y" = alloca i32
  store i32 3, i32* %"y"
  %"z" = alloca i32
  %"x.val" = load i32, i32* %"x"
  %"y.val" = load i32, i32* %"y"
  %".4" = mul i32 %"y.val", 2
  %".5" = add i32 %"x.val", %".4"
  store i32 %".5", i32* %"z"
  %"z.val" = load i32, i32* %"z"
  %".7" = bitcast [4 x i8]* @"fmt.0" to i8*
  %".8" = call i32 (i8*, ...) @"printf"(i8* %".7", i32 %"z.val")
  ret i32 0
}

@"fmt.0" = internal constant [4 x i8] c"%d\0a\00"