class congkak:
    # define board structure
    board = [7,7,7,7,7,7,7,0,7,7,7,7,7,7,7,0]
    hole = 0
    player = 0
    # Logics
    # - Sinks -> Player 1 can only fill hole 7, Player 2 can only 15
    # - Moving -> if meet sink, skip unless its corresponding.
    # - Moving II -> once pickup a hole, clear hole and do deduction 1by1.
    # - End move -> once last drop, perform a checking.
    # - Move check -> If the current hole == 1, end move. IF player in range to steal, do steal.
    # - MvCheck II -> if current hole > 1, proceed with another iteration of Moving.
    # - Steal function = create algo to correspond the hole values. ez, make 16 - holeNo. you gonna get the corresponding hole.
    # - ChgMove - ask for next player. use a flipping bit. XOR is chosen. set player as 0, use XOR to flip. [player ^= 1]

    def move(self):
        # start by clearing hole.
        moves = self.board[self.hole]
        self.board[self.hole] = 0
        # iterate according to number of moves.
        for x in range(moves):
            # iterate next hole first.
            self.hole += 1
            if (self.player == 0 and self.hole == 15) or (self.hole == 16):
                self.hole == 0
            elif (self.player == 1 and self.hole == 7):
                self.hole += 1
            self.board[self.hole] += 1

    def moveChk(self):
        # check if current hole is only drop.
        if self.board[self.hole] == 1:
            self.chkSteal(self)
        else:
            self.move(self)


    def steal(self):
        corr = 14 - self.hole
        # stealing, if player 0, steal and put in sink 0, else sink 15
        self.

    def chkSteal():


    def chgPlayer():

    def moveInput():

    