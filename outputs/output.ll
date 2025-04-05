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
  %"cmptmp" = icmp eq i32 %"x.1", 0
  br i1 %"cmptmp", label %"then.0", label %"else.0"
ifcont:
  ret i32 0
then.0:
  %"strptr.3" = getelementptr [5 x i8], [5 x i8]* @"str.2", i32 0, i32 0
  %"fmtptr" = getelementptr [4 x i8], [4 x i8]* @"fmt.3", i32 0, i32 0
  %".4" = call i32 (i8*, ...) @"printf"(i8* %"fmtptr", i8* %"strptr.3")
  br label %"ifcont"
else.0:
  %"strptr.5" = getelementptr [6 x i8], [6 x i8]* @"str.4", i32 0, i32 0
  %"fmtptr.1" = getelementptr [4 x i8], [4 x i8]* @"fmt.5", i32 0, i32 0
  %".6" = call i32 (i8*, ...) @"printf"(i8* %"fmtptr.1", i8* %"strptr.5")
  br label %"ifcont"
}

@"str.2" = internal constant [5 x i8] c"Nose\00"
@"fmt.3" = internal constant [4 x i8] c"%s\0a\00"
@"str.4" = internal constant [6 x i8] c"si se\00"
@"fmt.5" = internal constant [4 x i8] c"%s\0a\00"