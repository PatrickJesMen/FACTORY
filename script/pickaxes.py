from script.pickaxe import Pickaxe

def pickaxe_list(choice):
    match choice:
        case "Stone":
            return Pickaxe(name="Stone Pickaxe", damage=1, image= "models/pickaxes/stone_pickaxe.png" , value=0)
        case "Iron":
            return Pickaxe(name="Iron Pickaxe", damage=10, image= "models/pickaxes/iron_pickaxe.png" , value=350)
        case "Gold":
            return Pickaxe(name="Golden Pickaxe", damage=50, image= "models/pickaxes/gold_pickaxe.png" , value=2500)
        case "Diamond":
            return Pickaxe(name="Diamond Pickaxe", damage=150, image= "models/pickaxes/diamond_pickaxe.png" , value=15000)
        case "Emerald":
            return Pickaxe(name="Emerald Pickaxe", damage=500, image="models/pickaxes/emerald_pickaxe.png", value=100000)
        case "Rubi":
            return Pickaxe(name="Rubi Pickaxe", damage=2500, image="models/pickaxes/rubi_pickaxe.png", value=750000)
