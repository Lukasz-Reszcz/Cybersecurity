import tkinter as tk
from tkinter import ttk

import email_protocol as ep
import send_email as se

# TODO
# - add button to create random strings
# - selection of the private or public key

def generate_hash_value():
    # Get the entered value
    str1=str1_input.get()
    str2=str2_input.get()
    coin_flip_val=coin_flip_input.get()

    # Test if the strings are given correctly
    if(str1 == "" or str2 == "" or coin_flip_val == ""):
        print("Hash value con not be generated")

    # Create and write a hash value
    hash_value.config(state="normal")
    hash_value.delete(0, tk.END)    
    hash_value.insert(0, ep.hash_encryption(str1,str2,coin_flip_val))
    hash_value.config(state="readonly")

def see_email():
    # Create a new Toplevel window (separate from the main window)
    new_window = tk.Toplevel(root)
    new_window.title("Email draft")
    new_window.geometry("300x200")

    # Labels for email info
    from_label = tk.Label(new_window, text="From")
    from_label.grid(row=0, column=0)
    to_label = tk.Label(new_window, text="To")
    to_label.grid(row=1, column=0)

    # Edit fields (disabled) for email info
    from_draft = tk.Entry(new_window, state="normal")
    # Is delete neccessary?
    # from_entry.delete(0, tk.END) 
    from_draft.insert(0, from_email_input.get())
    from_draft.config(state="readonly")
    from_draft.grid(row=0, column=1)

    to_draft = tk.Entry(new_window, state="normal")
    to_draft.insert(0, to_email_input.get())
    to_draft.config(state="readonly")
    to_draft.grid(row=1, column=1)

    # subject, message (hash)
    subject_label = tk.Label(new_window, text="Subject")
    subject_label.grid(row=2, column=0)

    subject_draft = tk.Entry(new_window, state="normal")
    # Later replace Test with actual subject
    subject_draft.insert(0, "Coin flip hash value")
    subject_draft.config(state="readonly")
    subject_draft.grid(row=2, column=1)

    message_label = tk.Label(new_window, text="Message")
    message_label.grid(row=3, column=0)

    message_draft = tk.Entry(new_window, state="normal")
    message_draft.insert(0, hash_value.get())
    message_draft.config(state="readonly")
    message_draft.grid(row=3, column=1)

    # str1,str2, coinflipval
    str1_label_draft = tk.Label(new_window, text="String 1")
    str1_label_draft.grid(row=4, column=0)

    str1_draft = tk.Entry(new_window, state="normal")
    str1_draft.insert(0, str1_input.get())
    str1_draft.config(state="readonly")
    str1_draft.grid(row=4, column=1)

    str2_draft_label = tk.Label(new_window, text="String 2")
    str2_draft_label.grid(row=5, column=0)

    str2_draft = tk.Entry(new_window, state="normal")
    str2_draft.insert(0, str2_input.get())
    str2_draft.config(state="readonly")
    str2_draft.grid(row=5, column=1)

    coin_filp_val_label = tk.Label(new_window, text="Coin flip value")
    coin_filp_val_label.grid(row=6, column=0)

    coin_flip_val_draft = tk.Entry(new_window, state="normal")
    coin_flip_val_draft.insert(0, coin_flip_input.get())
    coin_flip_val_draft.config(state="readonly")
    coin_flip_val_draft.grid(row=6, column=1)

def make_random_string(button_option):
    if button_option == 0:
        str1_input.delete(0,tk.END)
        str1_input.insert(0, ep.generate_random_string())
    elif button_option == 1:
        str2_input.delete(0, tk.END)
        str2_input.insert(0, ep.generate_random_string())

def send_email_command():
    from_user = from_email_input.get() # 'a70904597@gmail.com'
    to_user = to_email_input.get() # 'p36494089@gmail.com'
    subject = "Hash Value"
    str1 = str1_input.get()
    hashed_val = hash_value.get()
    body = f'String 1: {str1}\nHash Value: {hashed_val}'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = from_email_input.get()
    smtp_password = 'nydv panh ofhz wtxi'

    # send email
    se.send_email(from_user, to_user, subject, body, smtp_server, smtp_port, smtp_user, smtp_password)
    
    # create log file OR write log data in the file if exists
    ep.create_log_file(from_user, to_user, str1, hashed_val)

# This function reads data sent by Alice to Bob
# from log file
def load_email_data(hash_value_entered):
    hash_value = 0

    with open('log.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            # Do until you meet the entered hash value
            if line.startswith('Hash value'):
                hash_value = line.split(':')[1].strip()

            if line.startswith('From'):
                bobs_to = line.split(':')[1].strip()

            if line.startswith('To'):
                bobs_from = line.split(':')[1].strip()

            if hash_value_entered == hash_value:
                # Clear the fields
                from_guess_input.delete(0, tk.END)
                to_guess_input.delete(0, tk.END)

                # Load the proper emails
                from_guess_input.insert(0, bobs_from)
                to_guess_input.insert(0, bobs_to)

                break

    
# Create the main window
root = tk.Tk()
root.title("Coin flip")
root.geometry("700x400")

# Create a frame for creating hash value
hash_frame = tk.Frame(root)

# Create a label widget
hash_title_label = tk.Label(hash_frame, text="Generate hash value")
hash_title_label.grid(row=0, column=0, columnspan=2)
str1_label = tk.Label(hash_frame, text="Enter String 1: ")
str1_label.grid(row=1, column=0, sticky="w")
str2_label = tk.Label(hash_frame, text="Enter String 2: ")
str2_label.grid(row=2, column=0, sticky="w")
coin_flip_label = tk.Label(hash_frame, text="Enter coin flip value: ")
coin_flip_label.grid(row=3, column=0, sticky="w")

# Create an input
str1_input = tk.Entry(hash_frame)
str1_input.grid(row=1, column=1)
str2_input = tk.Entry(hash_frame)
str2_input.grid(row=2, column=1)

# Create buttons to generate random string
circle_image = tk.PhotoImage(file='circle.png')
circle_image = circle_image.subsample(25, 25)


gen_str1_button = tk.Button(hash_frame, image=circle_image, command=lambda: make_random_string(0))
gen_str1_button.grid(row=1, column=2)

gen_str2_button = tk.Button(hash_frame, image=circle_image, command=lambda: make_random_string(1))
gen_str2_button.grid(row=2, column=2)

# Dropdown for coin flip value
coin_flip_input = ttk.Combobox(hash_frame, values=['head', 'tail'], state='readonly')
coin_flip_input.grid(row=3, column=1)

# show hash value
hash_label = tk.Label(hash_frame, text="Hash value")
hash_label.grid(row=5, column=0, sticky="w")
hash_value = tk.Entry(hash_frame, text="", state="disabled")
hash_value.grid(row=5, column=1)

# Create a button widget
button = tk.Button(hash_frame, text="Generate hash value", command=generate_hash_value)
button.grid(row=4, column=0)

# Add frame to the main grid
hash_frame.grid(row=0, column=0)

# Frame for email
email_frame = tk.Frame(root)

email_label = tk.Label(email_frame, text="Send hash value per email")
email_label.grid(row=0, column=0, columnspan=2)

# Label for the email
from_email_label = tk.Label(email_frame, text="From")
from_email_label.grid(row=1, column=0)
to_email_label = tk.Label(email_frame, text="To")
to_email_label.grid(row=2, column=0)

# Input for email data
from_email_input = tk.Entry(email_frame)
from_email_input.insert(0, 'a70904597@gmail.com') # For test purpose
from_email_input.grid(row=1, column=1)

to_email_input = tk.Entry(email_frame)
to_email_input.insert(0, 'p36494089@gmail.com') # For test purpose
to_email_input.grid(row=2, column=1)

# Button send email
send_email_button = tk.Button(email_frame, text="send email", command=send_email_command)
send_email_button.grid(row=3, column=0)
see_draft_button = tk.Button(email_frame, text="see email", command=see_email)
see_draft_button.grid(row=3, column=1)

# Add email frame to main grid
email_frame.grid(row=1, column=0, sticky="w")

# Create frame for Bob's choice (punishment)
guess_frame = tk.Frame(root)
guess_label = tk.Label(guess_frame, text='Guess the coin flip value')
guess_label.grid(row=0, column=0, columnspan=2)

# Add hash value label and input to load the data
hash_value_guess_label = tk.Label(guess_frame, text = 'Enter received hash value')
hash_value_guess_label.grid(row=1, column=0)

hash_value_guess_input = tk.Entry(guess_frame)
hash_value_guess_input.grid(row=1, column=1)

# Button to enter typed hash value
hash_value_guess_input_confirm = tk.Button(guess_frame, text='OK', \
                                            command=lambda: load_email_data(hash_value_guess_input.get()))
hash_value_guess_input_confirm.grid(row=1, column=2)

# Set field from and to to send a punishment
from_guess_label = tk.Label(guess_frame, text='From')
from_guess_input = tk.Entry(guess_frame)
to_guess_label = tk.Label(guess_frame, text='To')
to_guess_input = tk.Entry(guess_frame)

# Place field on the punishment frame
from_guess_label.grid(row=2, column=0)
from_guess_input.grid(row=2, column=1)
to_guess_label.grid(row=3, column=0)
to_guess_input.grid(row=3, column=1)

# 
coin_flip_label_guess = tk.Label(guess_frame, text="Enter coin flip value: ")
coin_flip_label_guess.grid(row=4, column=0, sticky='w')
coin_flip_input_guess = ttk.Combobox(guess_frame, values=['head', 'tail'], state='readonly')
coin_flip_input_guess.grid(row=4, column=1, sticky='w')


# Create a button to send the punishment
# TODO
# - Create a function to send punishment
# name of function without ''!
guess_value_button = tk.Button(guess_frame, text='send value guess', command='')
guess_value_button.grid(row=5, column=0)

# Add punishment grid to main grig
guess_frame.grid(row=0, column=1, sticky='w')

# Create frame to show email
# show_email_frame = tk.Frame(root)
# show_email_frame

# Create frame to reavel phase (Alice)
reveal_alice_frame = tk.Frame(root)
reveal_label = tk.Label(reveal_alice_frame, text='Reveal phase for (Alice)')
reveal_label.grid(row=0, column=0, columnspan=2)

# Create button to send reveal values
send_reveal_values_button = tk.Button(reveal_alice_frame, text='send reveal values', command='')
send_reveal_values_button.grid(row=1, column=0)

# Add reveal frame in main grid
reveal_alice_frame.grid(row=2, column=0, sticky='w')

# Start the GUI event loop
root.mainloop()