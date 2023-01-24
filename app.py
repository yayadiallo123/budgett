import sqlite3


connextion = sqlite3.connect('budget1.db') 
cursor = connextion.cursor()


def create_revenus():
        cursor.execute(
            
            "CREATE TABLE   revenus(id integer PRIMARY KEY  AUTOINCREMENT,designation VARCHAR(200),montant INT)"
        )
        
                
def create_depenses():
        cursor.execute(
            
            "CREATE TABLE   depenses(id integer PRIMARY KEY  AUTOINCREMENT,designation VARCHAR(200),montant INT)"
        )

def insertion_depenses():
        print("Entrer les Depenses : ")
    
        designation = input("entrer la designation : ")
        montant = int(input("entrer le montant : "))
        donnees = [designation,montant]
        cursor.execute("INSERT INTO depenses(Designation,montant) VALUES (?,?)", donnees)
        connextion.commit()
        
def insertion_revenus():
        print("ENTRER les Revenus : ")
    
        designation = input("entrer la designation : ")
        montant = int(input("entrer le montant : "))
        donnees = [designation,montant]
        cursor.execute("INSERT INTO revenus(Designation,montant) VALUES (?,?)", donnees)
        connextion.commit()
        
def afficher_depenses():
        cursor.execute("SELECT * FROM depenses")
        lignes = cursor.fetchall()
        for ligne in lignes:
            print(ligne)
def afficher_revenus():
        cursor.execute("SELECT * FROM revenus")
        lignes = cursor.fetchall()
        for ligne in lignes:
            print(ligne) 
            
            
def somme_depenses():
        cursor.execute("SELECT sum(montant)  FROM depenses")
        depenses = cursor.fetchone()
        print("Total des depenses : ", depenses[0])
            
def somme_Revenus():
        cursor.execute("SELECT sum(montant)  FROM revenus")
        revenus = cursor.fetchone()
        print("Total des REVENUS : ", revenus[0]) 
        
def Bilan():
        cursor.execute("SELECT sum(montant) from revenus")
        revenus= cursor.fetchone()
        resultat1 = revenus[0]
        print("sommes des revenus : ",resultat1)
        cursor.execute("SELECT sum(montant) from depenses ")
        depenses= cursor.fetchone()
        resultat2 = depenses[0]
        print("sommes des depenses : ",resultat2)
        ecart = resultat1-resultat2
        print(ecart)   
    
            
def modifier_depenses(id,new_valeur):
        id= int(input("donner l 'id : "))
        cursor.execute("UPDATE depenses SET designation = ? WHERE id = ? ", (new_valeur,id))
        connextion.commit()
        
        
def Menu_navigation():
        

            
        
        print('2 -- Creation _Table_revenus ')
        print('3 -- Inserer_Depenses')
        print('4 -- Inserer_revenu')
        print('5 ----- Afficher les Depenses ')
        print('6 ------ Afficher les Revenus')
        print('7 ------ Modifier les Depenses')
        print('8 -----Total des depenses -------')
        print('9------Total des Revenu  --------')
        print('10 ---------ECART ------------------')
        print('---------------------------------------')
        print('---------------------------------------')
        
            
            

             
        choix =int(input('Entrer le choix  : '))
        while choix != 0:
            if choix not in range(1,11):
                 print('Fait le CHoix ENTRE 1-10 ')
                 break
                 
                   
            else:
                if choix == 1:
                        print('1 -- Creation _Table_depenses ')
                        create_depenses()
                        print("table cree avec succes")
                elif choix  == 2:
                        create_revenus()
                        print("table revenu cree avec succes")
                elif choix == 3:
                        insertion_depenses()
                        print("Depenses ajoutes avec succes")
                elif choix== 4:
                        insertion_revenus()
                        print("Revenu ajoute avec Succes")
                    
                elif choix == 5:
                        afficher_depenses()
                    
                elif choix == 6:
                        afficher_revenus()
                elif choix == 7:
                        desig=input("donner la nouvelle valeur : ")
                        modifier_depenses(id,new_valeur=desig)
                        print("modification effectuee avec succes")
                elif choix == 8 :
                        somme_depenses()
                    
                elif choix == 9:
                        somme_Revenus()
                    
                elif choix==10:
                        Bilan()
                        
                elif choix==0:
                    break
                choix =int(input('Entrer le choix  : '))
        
                   
            
        
            
            
        
            
connextion.close




Menu_navigation()
