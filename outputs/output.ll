; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"primernumero" = alloca i32
  store i32 0, i32* %"primernumero"
  %"segundo" = alloca i32
  store i32 0, i32* %"segundo"
  ret i32 0
}
