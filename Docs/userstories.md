As a ___ I want ___

#Must  


As a nurse I want to get into the rooms of all my clients  
-    Test with door to which the nurse has access            (pass)  
-    Test with door to which the nurse has no access         (fail)  


As a nurse I want to get into the common areas  
-    Test with door to which the nurse has access            (pass)  
-    Test with door to which the nurse has no access         (fail)  


As a nurse I want to get into the nurse-only areas  
-    Test with door to which the nurse has access            (pass)  
-    Test with door to which the nurse has no access         (fail)  


As a client I want to get into my own room  
-    Test with door for the clients own room                 (pass)  
-    Test with door for another client’s room                (fail)  
-    Test with door for a door which the client used to own (fail)  


As a client I want to get into the common areas  
-    Test with door to which the client has access           (pass)  
-    Test with door to which the client has no access        (fail)  


As a doctor I want to get into all the rooms  
-    Test with door to which doctor has access              (pass)

As a system administrator I don’t want old ‘cards’ to be able to enter the rooms  
-    Test with door with a card that belongs to an old client/staff member (door should stay closed)                           (pass)  
-    Test with door with a card that belongs to a current client/staff member on a door he/she has access to (door should open) (fail)  


As a system administrator I want to be able to issue a new ‘card’  
-    Test with an old card                                   (fail)  
-    Test with a new card without access                     (pass)  


As a system administrator I want to be able to disable a ‘card’ (temporarily)  
-    Test with an enabled card                               (pass)  
-    Test with a disabled card                               (false)  


As a system administrator I want the UID of an RFID-tag to be sent securely between the arduino and the computer  


As a system administrator I want to be able to compare the UID of an RFID-tag with the saved UIDs in a database to check whether it is authorized or not.  
-    Test with a door with an authorized UID                 (pass)  
-    Test with a door with an non-authorized UID             (fail)  


As a system administrator I want to be able to save the UID of a RFID-tag in the database.  
-    Test with UID that’s not yet in the database            (pass)  
-    Test with UID that is already in the database           (fail)  


As a system administrator I want to be able to delete the UID of a RFID-tag from the database.  
-    Test with UID that’s not yet in the database            (fail)  
-    Test with UID that is already in the database           (pass)  


As a system administrator I want no users to be able to copy or see the authorized UID of a RFID-tag 


#Should


As a user I want visual or audible feedback when my card has been scanned
-   Test with a key for the scanner and hear a noise or see a light (pass)  
-   Test with a key and gain no feedback (fail)  


As a user I want visual or audible feedback regarding my authorization status
-   Test on an door and hear or see something (pass)  
-   Test on an unauthorized door and hear or see nothing (fail)  


#Could


As a system administrator I want to revoke all access to a door  


As a team manager I want to be able to control the authorization of all cards and doors belongs to my team  


#Won't


As a team manager I want to see who opened which door at what time  


As a team manager I want to see who is authorized to open a specific door  


As a team manager I want to see how many cards are authorized at any given time  


As a system administrator I want to authorize keys of visitors  


As a visitor I want to have access to the common areas during visitor hours  
-   Test being able to enter the common area (pass)  
-   Test not being able to enter the common area (fail)  


As a client I want to (temporarily) authorize specific cards which belong to my family members  


As a system administrator I want to open all the doors at any time in case of an emergency  





