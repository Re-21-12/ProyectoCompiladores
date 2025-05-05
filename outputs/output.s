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
	movl	$2, 4(%rsp)
	movl	$fmt.2, %edi
	movl	$2, %esi
	xorl	%eax, %eax
	callq	printf@PLT
	xorl	%eax, %eax
	popq	%rcx
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
