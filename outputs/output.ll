; ModuleID = "main_module"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"contador" = alloca i32
  store i32 0, i32* %"contador"
  %"suma" = alloca i32
  store i32 0, i32* %"suma"
  %"suma2" = alloca i32
  store i32 0, i32* %"suma2"
  %"mensaje" = alloca i8*
  %"strptr" = getelementptr [21 x i8], [21 x i8]* @"str.0", i32 0, i32 0
  store i8* %"strptr", i8** %"mensaje"
  %"es_valido" = alloca i1
  store i1 1, i1* %"es_valido"
  %"es_admin" = alloca i1
  store i1 0, i1* %"es_admin"
  %"contador2" = alloca i32
  store i32 0, i32* %"contador2"
  %"suma3" = alloca i32
  store i32 0, i32* %"suma3"
  %"suma4" = alloca i32
  store i32 0, i32* %"suma4"
  %"mensaje1" = alloca i8*
  %"strptr.1" = getelementptr [21 x i8], [21 x i8]* @"str.1", i32 0, i32 0
  store i8* %"strptr.1", i8** %"mensaje1"
  %"es_valido2" = alloca i1
  store i1 1, i1* %"es_valido2"
  %"mensaje.val" = load i8*, i8** %"mensaje"
  %".13" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i8* %"mensaje.val")
  %"resultado1" = alloca i32
  %".15" = add i32 5, 3
  store i32 %".15", i32* %"resultado1"
  %"resultado2" = alloca i32
  %".17" = sub i32 10, 2
  store i32 %".17", i32* %"resultado2"
  %"resultado3" = alloca i32
  %".19" = mul i32 4, 7
  store i32 %".19", i32* %"resultado3"
  %"resultado4" = alloca double
  %".21" = fdiv double 0x4034000000000000, 0x4010000000000000
  store double %".21", double* %"resultado4"
  %"resultado1.val" = load i32, i32* %"resultado1"
  %".23" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".24" = call i32 (i8*, ...) @"printf"(i8* %".23", i32 %"resultado1.val")
  %"resultado2.val" = load i32, i32* %"resultado2"
  %".25" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".26" = call i32 (i8*, ...) @"printf"(i8* %".25", i32 %"resultado2.val")
  %"resultado3.val" = load i32, i32* %"resultado3"
  %".27" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".28" = call i32 (i8*, ...) @"printf"(i8* %".27", i32 %"resultado3.val")
  %"resultado4.val" = load double, double* %"resultado4"
  %".29" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", double %"resultado4.val")
  %"total" = alloca i32
  %"resultado1.val.1" = load i32, i32* %"resultado1"
  %"resultado2.val.1" = load i32, i32* %"resultado2"
  %".31" = add i32 %"resultado1.val.1", %"resultado2.val.1"
  store i32 %".31", i32* %"total"
  %"total2" = alloca i32
  %"resultado3.val.1" = load i32, i32* %"resultado3"
  %"resultado1.val.2" = load i32, i32* %"resultado1"
  %".33" = mul i32 %"resultado3.val.1", %"resultado1.val.2"
  store i32 %".33", i32* %"total2"
  %"total.val" = load i32, i32* %"total"
  %".35" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".36" = call i32 (i8*, ...) @"printf"(i8* %".35", i32 %"total.val")
  br i32 0, label %"if.then", label %"if.end"
if.then:
  br label %"if.end"
if.end:
  %"i" = alloca i32
  store i32 0, i32* %"i"
  br label %"for.cond"
for.cond:
  %"i.val" = load i32, i32* %"i"
  %".41" = icmp slt i32 %"i.val", 19
  br i1 %".41", label %"for.body", label %"for.end"
for.body:
  %"suma.val" = load i32, i32* %"suma"
  %"i.val.1" = load i32, i32* %"i"
  %".43" = add i32 %"suma.val", %"i.val.1"
  store i32 %".43", i32* %"suma"
  %"suma.val.1" = load i32, i32* %"suma"
  %".45" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".46" = call i32 (i8*, ...) @"printf"(i8* %".45", i32 %"suma.val.1")
  br label %"for.update"
for.update:
  br label %"for.cond"
for.end:
  br label %"while.cond"
while.cond:
  %"suma.val.2" = load i32, i32* %"suma"
  %".50" = icmp slt i32 %"suma.val.2", 20
  br i1 %".50", label %"while.body", label %"while.end"
while.body:
  %"suma.val.3" = load i32, i32* %"suma"
  %".52" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".53" = call i32 (i8*, ...) @"printf"(i8* %".52", i32 %"suma.val.3")
  br label %"while.cond"
while.end:
}

@"str.0" = internal constant [21 x i8] c"Comenzando algoritmo\00"
@"str.1" = internal constant [21 x i8] c"Comenzando algoritmo\00"
@"fmt.1" = internal constant [4 x i8] c"%s\0a\00"
@"fmt.2" = internal constant [4 x i8] c"%d\0a\00"
@"fmt.3" = internal constant [4 x i8] c"%f\0a\00"
define i32 @"calcularMultiplicacion"(i32 %".1", i32 %".2")
{
entry:
  %"a.addr" = alloca i32
  store i32 %".1", i32* %"a.addr"
  %"b.addr" = alloca i32
  store i32 %".2", i32* %"b.addr"
  %"resultado" = alloca i32
  %"a.val" = load i32, i32* %"a.addr"
  %"b.val" = load i32, i32* %"b.addr"
  %".6" = mul i32 %"a.val", %"b.val"
  store i32 %".6", i32* %"resultado"
  %"resultado.val" = load i32, i32* %"resultado"
  %".8" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %"resultado.val")
  %"resultado.val.1" = load i32, i32* %"resultado"
  ret i32 %"resultado.val.1"
}

define double @"calcularPromedio"(double %".1", double %".2")
{
entry:
  %"total.addr" = alloca double
  store double %".1", double* %"total.addr"
  %"cantidad.addr" = alloca double
  store double %".2", double* %"cantidad.addr"
  %"promedio" = alloca double
  %"total.val" = load double, double* %"total.addr"
  %"cantidad.val" = load double, double* %"cantidad.addr"
  %".6" = fdiv double %"total.val", %"cantidad.val"
  store double %".6", double* %"promedio"
  %"promedio.val" = load double, double* %"promedio"
  %".8" = bitcast [4 x i8]* @"fmt.3" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", double %"promedio.val")
  %"promedio.val.1" = load double, double* %"promedio"
  ret double %"promedio.val.1"
  %".11" = call i32 @"calcularMultiplicacion"(i32 4, i32 6)
  %".12" = call double @"calcularPromedio"(double 0x4041c00000000000, double 0x4014000000000000)
}

define i1 @"esParFunc"(i32 %".1")
{
entry:
  %"numero.addr" = alloca i32
  store i32 %".1", i32* %"numero.addr"
  br i32 0, label %"if.then", label %"if.else"
if.then:
  br label %"if.end"
if.end:
  %"par" = alloca i1
  store i1 1, i1* %"par"
  br i32 0, label %"if.then.1", label %"if.else.1"
if.else:
  ret i1 0
if.then.1:
  br label %"if.end.1"
if.end.1:
  %"x" = alloca i32
  store i32 0, i32* %"x"
  br label %"for.cond"
if.else.1:
  %"strptr" = getelementptr [22 x i8], [22 x i8]* @"str.4", i32 0, i32 0
  %".10" = bitcast [4 x i8]* @"fmt.1" to i8*
  %".11" = call i32 (i8*, ...) @"printf"(i8* %".10", i8* %"strptr")
  br label %"if.end.1"
for.cond:
  %"x.val" = load i32, i32* %"x"
  %".15" = icmp slt i32 %"x.val", 1000
  br i1 %".15", label %"for.body", label %"for.end"
for.body:
  %"suma2.val" = load i32, i32* %"suma2"
  %"x.val.1" = load i32, i32* %"x"
  %".17" = add i32 %"suma2.val", %"x.val.1"
  store i32 %".17", i32* %"suma2"
  %"suma2.val.1" = load i32, i32* %"suma2"
  %".19" = bitcast [4 x i8]* @"fmt.2" to i8*
  %".20" = call i32 (i8*, ...) @"printf"(i8* %".19", i32 %"suma2.val.1")
  br label %"for.update"
for.update:
  br label %"for.cond"
for.end:
}

@"str.4" = internal constant [22 x i8] c"El resultado es impar\00"