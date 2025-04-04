; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 5, i32* %"x"
  %"y" = alloca i32
  store i32 3, i32* %"y"
  %"x.1" = load i32, i32* %"x"
  %"y.1" = load i32, i32* %"y"
  %"multmp" = mul i32 %"y.1", 2
  %"addtmp" = add i32 %"x.1", %"multmp"
  %"z" = alloca i32
  store i32 %"addtmp", i32* %"z"
  %"z.1" = load i32, i32* %"z"
  %"fmtptr" = getelementptr [4 x i8], [4 x i8]* @"fmt.2", i32 0, i32 0
  %".5" = call i32 (i8*, ...) @"printf"(i8* %"fmtptr", i32 %"z.1")
  ret i32 0
}

@"fmt.2" = internal constant [4 x i8] c"%d\0a\00"