; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 1, i32* %"x"
  %"x.1" = load i32, i32* %"x"
  %"incrtmp" = add i32 %"x.1", 1
  store i32 %"incrtmp", i32* %"x"
  %"x.2" = load i32, i32* %"x"
  %"fmtptr" = getelementptr [4 x i8], [4 x i8]* @"fmt.2", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"fmtptr", i32 %"x.2")
  ret i32 0
}

@"fmt.2" = internal constant [4 x i8] c"%d\0a\00"