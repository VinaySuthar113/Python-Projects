import customtkinter as ctk
from tkinter import messagebox
import matplotlib.pyplot as plt

class VotingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Voting System")

        self.parties = []
        self.voters = set()
        self.votes = {}
        self.verified_voter = None

        self.setup_ui()

    def setup_ui(self):
        ctk.CTkLabel(self.root, text="Enter Party Name:").grid(row=0, column=0, pady=10, padx=10)
        self.party_entry = ctk.CTkEntry(self.root)
        self.party_entry.grid(row=0, column=1, pady=10, padx=10)
        ctk.CTkButton(self.root, text="Add Party", command=self.add_party).grid(row=0, column=2, pady=10, padx=10)

        ctk.CTkLabel(self.root, text="Enter Party Name to Remove:").grid(row=1, column=0, pady=10, padx=10)
        self.remove_party_entry = ctk.CTkEntry(self.root)
        self.remove_party_entry.grid(row=1, column=1, pady=10, padx=10)
        ctk.CTkButton(self.root, text="Remove Party", command=self.remove_party).grid(row=1, column=2, pady=10, padx=10)

        ctk.CTkButton(self.root, text="View Parties", command=self.view_parties).grid(row=2, column=0, columnspan=2, pady=10, padx=10)
        ctk.CTkButton(self.root, text="Submit Parties", command=self.submit_parties).grid(row=2, column=2, pady=10, padx=10)

        self.party_frame = ctk.CTkFrame(self.root)
        self.party_frame.grid(row=3, column=0, columnspan=3, pady=10, padx=10, sticky='nsew')
        self.party_frame.grid_columnconfigure(0, weight=1)
        
        ctk.CTkLabel(self.root, text="Enter Voter Name:").grid(row=4, column=0, pady=10, padx=10)
        self.voter_entry = ctk.CTkEntry(self.root)
        self.voter_entry.grid(row=4, column=1, pady=10, padx=10)
        ctk.CTkButton(self.root, text="Verify Vote", command=self.verify_vote).grid(row=4, column=2, pady=10, padx=10)

        self.voting_frame = ctk.CTkFrame(self.root)
        self.voting_frame.grid(row=5, column=0, columnspan=3, pady=10, padx=10, sticky='nsew')
        self.voting_frame.grid_columnconfigure(0, weight=1)

        self.end_button = ctk.CTkButton(self.root, text="END Voting", command=self.end_voting)
        self.end_button.grid(row=6, column=0, columnspan=3, pady=10, padx=10)

    def add_party(self):
        party_name = self.party_entry.get().strip()
        if party_name:
            if party_name not in self.parties:
                self.parties.append(party_name)
                self.votes[party_name] = 0
                messagebox.showinfo("Success", f"Party '{party_name}' added.")
            else:
                messagebox.showwarning("Warning", "Party already exists.")
        self.party_entry.delete(0, ctk.END)

    def remove_party(self):
        party_name = self.remove_party_entry.get().strip()
        if party_name == "All":
            self.parties.clear()
            self.votes.clear()
            messagebox.showinfo("Success", "All parties removed.")
        elif party_name in self.parties:
            self.parties.remove(party_name)
            del self.votes[party_name]
            messagebox.showinfo("Success", f"Party '{party_name}' removed.")
        else:
            messagebox.showwarning("Warning", "Party not found.")
        self.remove_party_entry.delete(0, ctk.END)

    def view_parties(self):
        if self.parties:
            party_list = "\n".join(self.parties)
            messagebox.showinfo("Party List", party_list)
        else:
            messagebox.showwarning("Warning", "No parties added.")

    def submit_parties(self):
        if self.parties:
            messagebox.showinfo("Success", "Parties submitted successfully.")
            self.party_entry.configure(state='disabled')
            self.remove_party_entry.configure(state='disabled')
            self.party_frame.grid_forget()
            self.display_parties_for_voting()
        else:
            messagebox.showwarning("Warning", "No parties to submit.")

    def display_parties_for_voting(self):
        for widget in self.voting_frame.winfo_children():
            widget.destroy()
        for idx, party in enumerate(self.parties, start=1):
            party_label = ctk.CTkLabel(self.voting_frame, text=f"{idx}. {party}")
            party_label.grid(row=idx, column=0, pady=5, padx=5, sticky='w')
            vote_button = ctk.CTkButton(self.voting_frame, text="Vote", command=lambda p=party: self.cast_vote(p))
            vote_button.grid(row=idx, column=1, pady=5, padx=5)

    def verify_vote(self):
        voter_name = self.voter_entry.get().strip()
        if voter_name:
            if voter_name not in self.voters:
                self.verified_voter = voter_name
                self.voter_entry.configure(state='disabled')
                messagebox.showinfo("Verified", "Voter verified. You can now cast your vote.")
            else:
                messagebox.showwarning("Warning", "This voter has already voted.")
        else:
            messagebox.showwarning("Warning", "Enter a valid voter name.")

    def cast_vote(self, party):
        if self.verified_voter:
            self.votes[party] += 1
            self.voters.add(self.verified_voter)
            self.verified_voter = None
            self.voter_entry.configure(state='normal')
            self.voter_entry.delete(0, ctk.END)
            messagebox.showinfo("Success", f"Vote cast for {party}")
        else:
            messagebox.showwarning("Warning", "Please verify voter name first.")

    def end_voting(self):
        if self.votes:
            winner = max(self.votes, key=self.votes.get)
            result_message = f"Voting Ended.\n\nWinner: {winner}\nVotes: {self.votes[winner]}"
            messagebox.showinfo("Result", result_message)
            self.display_bar_graph()
        else:
            messagebox.showwarning("Warning", "No votes cast.")

    def display_bar_graph(self):
        parties = list(self.votes.keys())
        votes = list(self.votes.values())

        plt.figure(figsize=(10, 6))
        plt.bar(parties, votes, color='blue')
        plt.xlabel('Parties')
        plt.ylabel('Number of Votes')
        plt.title('Voting Results')
        plt.show()

if __name__ == "__main__":
    root = ctk.CTk()
    voting_system = VotingSystem(root)
    root.mainloop()
