	.text
	.file	"output.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$3, %edi
	movl	$4, %esi
	callq	primerafuncion@PLT
	xorl	%eax, %eax
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.globl	primerafuncion                  # -- Begin function primerafuncion
	.p2align	4, 0x90
	.type	primerafuncion,@function
primerafuncion:                         # @primerafuncion
	.cfi_startproc
# %bb.0:                                # %entry
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	%edi, 4(%rsp)
	movl	%esi, (%rsp)
	movl	$fmt.4, %edi
	movl	$str.3, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	movl	4(%rsp), %eax
	addl	(%rsp), %eax
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end1:
	.size	primerafuncion, .Lfunc_end1-primerafuncion
	.cfi_endproc
                                        # -- End function
	.type	str.3,@object                   # @str.3
	.section	.rodata,"a",@progbits
str.3:
	.asciz	"holamnudo"
	.size	str.3, 10

	.type	fmt.4,@object                   # @fmt.4
fmt.4:
	.asciz	"%s\n"
	.size	fmt.4, 4

	.section	".note.GNU-stack","",@progbits
