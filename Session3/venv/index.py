import functions

mDopusk = functions.getDopusk()
mLines, mNames, mScores = functions.getNamesAndScores()
mMiddles = functions.changeStrings1(mLines, mNames, mScores)
functions.changeStrings2(mLines, mScores)

mGoodRating, mBadRating = functions.makeRating(mLines, mMiddles, mDopusk)
functions.sortRatingByName(mBadRating)
