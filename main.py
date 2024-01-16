import tkinter as tk
from tkinter import messagebox
import random


class TriviaGame:

  def __init__(self, root):
    self.root = root
    self.root.title("Trivia Game")
    root.geometry("600x600")
    root.config(bg="#809fff")

    self.sports_questions = [{
        "question":
        "What is the regulation height of a basketball hoop in the NBA?",
        "answer":
        "10 feet",
        "options": ["9 feet", "9.5 feet", "10 feet", "10.5 Feet"]
    }, {
        "question":
        "Who is the all-time leading goal scorer in FIFA World Cup history?",
        "answer":
        "Miroslav Klose",
        "options":
        ["Lionel Messi", "Cristiano Ronaldo", "Pele", "Miroslav Klose"]
    }, {
        "question":
        "Which Grand Slam tournament is played on a grass court?",
        "answer":
        "Wimbledon",
        "options": ["Wimbledon", "Australian Open", "French Open", "US Open"]
    }, {
        "question":
        "In American football, how many points is a touchdown worth?",
        "answer":
        "6 points",
        "options": ["4 points", "6 points", "7 points", "8 points"]
    }, {
        "question":
        "Who holds the record for the most Olympic gold medals in swimming?",
        "answer":
        "Michael Phelps",
        "options":
        ["Michael Phelps", "Ian Thorpe", "Ryan Lochte", "Mark Spitz"]
    }, {
        "question":
        "Who holds the world record for the men's 100 meters sprint?",
        "answer":
        "Usain Bolt",
        "options":
        ["Noah Lyles", "Usain Bolt", "Justin Gatlin", "Yohan Blake"]
    }, {
        "question":
        "Who won Super Bowl LIV in 2020?",
        "answer":
        "Kansas City Chiefs",
        "options": [
            "New England Patriots", "Kansas City Chiefs",
            "San Francisco 49ers", "Los Angeles Rams"
        ]
    }, {
        "question":
        "Who is the all-time home run leader in Major League Baseball (MLB)?",
        "answer":
        "Barry Bonds",
        "options":
        ["Barry Bonds", "Babe Ruth", "Hank Aaron", "Alex Rodriguez"]
    }, {
        "question":
        "In ice hockey, what is it called when a player scores three goals in a single game?",
        "answer":
        "Hat trick",
        "options": ["Faceoff", "Slap shot", "Hat trick", "Power play"]
    }, {
        "question":
        "What is the name of the circuit that hosts the Monaco Grand Prix in Formula 1?",
        "answer":
        "Circuit de Monaco",
        "options": [
            "Monza", "Circuit de Barcelona-Catalunya", "Circuit de Monaco",
            "Silverstone"
        ]
    }]

    self.geography_questions = [{
        "question":
        "What is the capital of France?",
        "answer":
        "Paris",
        "options": ["Madrid", "Berlin", "Paris", "Rome"]
    }, {
        "question":
        "In which continent is the Sahara Desert located?",
        "answer":
        "Africa",
        "options": ["Asia", "Europe", "Africa", "South America"]
    }, {
        "question":
        "Which river is the longest in the world?",
        "answer":
        "Nile",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"]
    }, {
        "question":
        "What is the smallest country in the world?",
        "answer":
        "Vatican City",
        "options": ["Vatican City", "Malta", "Monaco", "Grenada"]
    }, {
        "question":
        "What is the capital of Japan?",
        "answer":
        "Tokyo",
        "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"]
    }, {
        "question":
        "Where is Mt Everest located?",
        "answer":
        "Himalaya",
        "options": ["Dhaulagiri", "Himalaya", "Karakoram", "Annapurna"]
    }, {
        "question":
        "What is the currency of Brazil?",
        "answer":
        "Brazilian Real",
        "options": ["Peso", "Ruble", "Yen", "Brazilian Real"]
    }, {
        "question":
        "What are the two countries with the longest international border",
        "answer":
        "Canada - United States",
        "options": [
            "China - Mongila", "Kazakstan - Russia", "Argentina - Chile",
            "Mexico - United States"
        ]
    }, {
        "question":
        "What are the four oceans of the world?",
        "answer":
        "Pacific, Atlantic, Indian, Arctic",
        "options": [
            "Pacific, Atlantic, Indian, Arctic",
            "Pacific, Atlantic, Dead Sea, Southern Ocean"
        ]
    }, {
        "question":
        "Which river is the longest in the world?",
        "answer":
        "Nile",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"]
    }]

    self.food_questions = [
        {
            "question":
            "Which cuisine is known for dishes like sushi, sashimi, and ramen?",
            "answer": "Japanese",
            "options": ["Italian", "Japanese", "Mexican", "Chinese"]
        },
        {
            "question":
            "In what year did McDonald's introduce the first Happy Meal?",
            "answer": "1983",
            "options": ["1975", "1983", "1991", "2002"]
        },
        {
            "question":
            "What is the main ingredient in the traditional French dessert, crème brûlée?",
            "answer": " Custard",
            "options":
            ["Chocolate", "Caramelized Sugar", "Custard", "Puff Pastry"]
        },
        {
            "question":
            "Which tea is known for its strong flavor and dark color, often served with milk?",
            "answer":
            "English Breakfast Tea",
            "options": [
                "English Breakfast Tea", "Green Tea", "Earl Grey Tea",
                "Chamomile Tea"
            ]
        },
        {
            "question":
            "What is the primary spice used in the Indian dish curry?",
            "answer": "Turmeric",
            "options": ["Paprika", "Cumin", "Turmeric", "Oregano"]
        },
        {
            "question":
            "Which type of cheese is typically used in Italian dishes like lasagna and pizza?",
            "answer": "Mozzarella",
            "options": ["Cheddar", "Swiss", "Brie", "Mozzarella"]
        },
        {
            "question": "Which vegetable is a key ingredient in guacamole?",
            "answer": "Avocado",
            "options": ["Onion", "Avocado", "Bell Pepper", "Tomato"]
        },
    ]

    self.categories = {
    "Food": self.food_questions,
    "Geography": self.geography_questions, 
    "Sports": self.sports_questions,
    }

    self.current_category = None
    self.current_question_index = 0

    self.create_widgets()

  def create_widgets(self):
    self.play_button = tk.Button(self.root,
                                 text="Play",font=("Monaco (monospace)", 20, "bold"),
                                 command=self.start_game)
    self.play_button.pack(pady=20)

  def start_game(self):
    self.play_button.pack_forget()

    self.question_category_label = tk.Label(self.root,
                                            text="Select a category:")
    self.question_category_label.pack(pady=20) #

    food_button = tk.Button(self.root,
                            text="Food",
                            command=lambda:
                            self.select_category("Food"))
    food_button.pack()

    geography_button = tk.Button(
        self.root,
        text="Geography",
        command=lambda: 
      self.select_category("Geography"))
    geography_button.pack()

    sports_button = tk.Button(self.root,
                              text="Sports",
                              command=lambda:
                              self.select_category("Sports"))
    sports_button.pack()


  def select_category(self, category):
    self.current_category = category
    self.show_question()
    self.question_category_label.destroy()

  def show_question(self):
    if self.current_category is not None and self.current_question_index < len(
        self.categories[self.current_category]):
      question_data = self.categories[self.current_category][
          self.current_question_index]

      self.question_label = tk.Label(
          self.root, text=f"Trivia Question: {question_data['question']}")
      self.question_label.pack(pady=20)

      self.answer_var = tk.StringVar()
      self.answer_var.set("")

      random.shuffle(question_data["options"])  # Shuffle the options

      
      for i, option in enumerate(question_data["options"]):
        self.op_b=tk.Radiobutton(self.root,
                       text=option,
                       variable=self.answer_var,
                       value=option).pack()

      self.submit_button = tk.Button(self.root,
                                     text="Submit",
                                     command=self.submit)
      self.submit_button.pack(pady=20)
    else:
      messagebox.showinfo("Game Over",
                          "You've completed all questions in this category!")

  def submit(self):
    self.check_answer()
    self.clear_options()

  def clear_options(self):
    for widget in self.root.winfo_children():
      widget.destroy()
    self.show_question()
    
    
  def check_answer(self):
    if self.current_category is not None and self.current_question_index < len(
        self.categories[self.current_category]):
      correct_answer = self.categories[self.current_category][
          self.current_question_index]["answer"]
      answer = self.answer_var.get()
      if answer == correct_answer:
        messagebox.showinfo("Correct", "Your answer is correct!")
        self.clear_options()
      else:
        messagebox.showinfo("Wrong!," f"the correct answer is {correct_answer}.")
        self.clear_options()

      # Destroy current widgets to prepare for the next question
      #self.question_label.destroy()
      #self.submit_button.destroy()
      
      self.current_question_index += 1

      

      self.show_question()


if __name__ == "__main__":
  root = tk.Tk()
  game = TriviaGame(root)
  root.mainloop()
