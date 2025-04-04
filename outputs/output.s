	.text
	.file	"output.ll"
	.globl	main                            # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:                                # %entry
	subq	$24, %rsp
	.cfi_def_cfa_offset 32
	movl	$5, 20(%rsp)
	movl	$3, 16(%rsp)
	movl	$11, 12(%rsp)
	movl	$fmt.2, %edi
	movl	$11, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	xorl	%eax, %eax
	addq	$24, %rsp
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc
                                        # -- End function
	.type	fmt.2,@object                   # @fmt.2
	.section	.rodata,"a",@progbits
fmt.2:
	.asciz	"%d\n"
	.size	fmt.2, 4

	.section	".note.GNU-stack","",@progbits
