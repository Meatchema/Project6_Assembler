// code snippet
// sum = 0
// i = 0
// while i < 100
//    sum = sum + 1
//    i = i + 1

@sum
M = 0
@i
M = 0

(LOOP)
@i
D = M
@END
D;JGE
D = D-M
@LOOP
D;JNE
@j
(END)
@k