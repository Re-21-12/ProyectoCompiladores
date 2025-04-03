; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"call.primerafuncion" = call i32 @"primerafuncion"(i32 3, i32 4)
  ret i32 0
}

define i32 @"primerafuncion"(i32 %"numerouno", i32 %"numerodos")
{
entry:
  %"numerouno.1" = alloca i32
  store i32 %"numerouno", i32* %"numerouno.1"
  %"numerodos.1" = alloca i32
  store i32 %"numerodos", i32* %"numerodos.1"
  %"strptr.4" = getelementptr [10 x i8], [10 x i8]* @"str.3", i32 0, i32 0
  %"fmtptr" = getelementptr [4 x i8], [4 x i8]* @"fmt.4", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %"fmtptr", i8* %"strptr.4")
  %"numerouno.2" = load i32, i32* %"numerouno.1"
  %"numerodos.2" = load i32, i32* %"numerodos.1"
  %"addtmp" = add i32 %"numerouno.2", %"numerodos.2"
  ret i32 %"addtmp"
}

@"str.3" = internal constant [10 x i8] c"holamnudo\00"
@"fmt.4" = internal constant [4 x i8] c"%s\0a\00"