def start_quiz():
    score = 0
    print("Should you share OTP?")
    print("a)Yes  b) No ")
    ans = input("Answer:")
    if ans.lower() == "b" :
        score += 1 
        print("score" , score)
  
