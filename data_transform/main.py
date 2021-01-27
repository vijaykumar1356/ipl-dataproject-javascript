import question1
import question2
import question3
import question4

if __name__ == '__main__':
    try:
    	question1.solution()
    	question2.solution()
    	question3.solution()
    	question4.solution()
    except FileNotFoundError as e:
    	print(e)
