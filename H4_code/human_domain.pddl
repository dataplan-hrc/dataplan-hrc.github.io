(define (domain HRI_dom)


(:requirements :strips :negative-preconditions :typing :disjunctive-preconditions :action-costs :conditional-effects)


(:types 
        location obj receptacle - object ; supertype
        food tobake drink slicable ToFry ToBoil ToRoast  sensitive_obj - obj 
        slicable - food
        vegetable fruit - slicable
        mobileR immobileR - receptacle
        fragile_receptacle - mobileR
)


(:constants
    
    Kitchen Bathroom LivingRoom StoreRoom - location
  
    Faucet Burner oven_switch Remaining_food Remaining_fruit Remaining_baked Remaining_veggy remaining_pizza Dirtydishes Dishwasher_Switch cleaned_dishes extinguisher pizza_base Sauce veggy prepared_pizza_base baked_pizza DustingCloth Clothes Cleaned_clothes Ironed_Clothes folded_clothes washingmachine_Switch Vacuum_Cleaner TV MusicPlayer Computer DustMop trash Medicines Color_lights Laptop_Switch water_bottle - obj

    stove_burner_1 stove_burner_2 stove_burner_3 stove_burner_4 sink countertop oven dustbin_1  fridge shelf rack cabinet washingmachine laundrybag ironing_board closet dining_table working_table - immobileR
    
    pan_1 pan_2 metal_pot office_bag tray tray_with_food - mobileR

    glass_1 plate_1 bowl_1 glass_2 plate_2 bowl_2 - fragile_receptacle
)


(:predicates
 
(human_near ?r - immobileR ?l - location)
(Human_at ?l - location)
(receptacle_at ?r1 - mobileR ?r2 - immobileR ?l - location)
(B_obj_at ?o - obj ?l - location)
(stuff_at ?o - obj ?r - immobileR ?l - location)
(human_switched_on ?o - obj ?r - immobileR ?l - location)
(human_switched_off ?o - obj ?r - immobileR ?l - location)
(In_human_hand ?o - obj)
(In_human_handB ?o - obj)
(InHumanHand ?r - mobileR)
(cleaned ?o - obj)
(sliced ?o - obj)
(cooked ?o - obj)
(not_fragile ?r - mobileR)
(fruit_served ?o - fruit ?r1 - mobileR ?r2 - immobileR ?l - location)
(food_served ?o - food ?r1 - mobileR ?r2 - immobileR ?l - location)
(baked_served ?o - tobake ?r1 - mobileR ?r2 - immobileR ?l - location)
(equal ?o1 ?o2 - obj)
(baked ?o - tobake)
(served_drink ?o1 - drink ?r1 - mobileR ?r2 - immobileR ?l - location)
(veggy_served ?o1 - vegetable ?r1 - mobileR ?r2 - immobileR ?l - location)
(open ?r - immobileR ?l - location)
(cleaned_remaining_food ?o - obj)
(dishes_cleaned)
(FireExtinguished ?l - location)
(pizza_baked)
(pizza_base_prepared)
(pizza_served ?r1 - mobileR ?r2 - immobileR ?l - location)
(washed_clothes)
(Ironedclothes)
(clothes_folded)
(laundrydone)
(human_switch_off ?o - obj)
(human_switch_on ?o - obj ?l - location)
(room_cleaned ?l - location)
(all_rooms_cleaned)
(electronics_cleaned ?o - obj ?l - location)
(electronic_items_Cleaned)
(human_hold ?o - object ?l - location)
(boiled ?o2 - obj)
(roasted ?o - obj)
(egg_prepared ?o - obj)
(item_in ?o - obj ?r1 - mobileR ?r2 - immobileR ?l - location)
(r_at ?r - immobileR ?l - location)
(salad_prepared ?o1 ?o2 ?o3 - obj)
(salad ?o - obj)
(prepared ?o - obj)
(bag_prepared ?o1 - obj ?o2 - obj ?o3 - obj)
(prepared_clothes ?o - obj ?r - immobileR ?l - location)
(human_hands_occupied_wo)
(human_hands_occupied_wr)
(heavy_obj_in_human_hand)
(not_burner ?r - immobileR)
(receptacle_cleaned ?o - receptacle ?l - location)
(office_ready)

 (party_at ?l - location)
 (charged ?o - obj)
 (medicines_provided_at ?r - immobileR ?l - location)

)

(:functions 
    (total-cost)

    (human_dur ?r1 ?r2 - receptacle)
)


;; Low level tasks



    
; Move between receptacles
(:action Human_moves_BR
 :parameters(?r1 ?r2 - immobileR ?l1 ?l2 - location)
 :precondition(and(human_near ?r1 ?l1) 
                  (human_at ?l1)
                  (r_at ?r1 ?l1)
                  (r_at ?r2 ?l2)
                  )           
 :effect(and(not(human_near ?r1 ?l1))
            (not(Human_at ?l1))
            (Human_at ?l2)
            (human_near ?r2 ?l2)
            (increase(total-cost)(human_dur ?r1 ?r2)) ;human_fast
        )                    
 )  


; Switching on stuff

(:action Human_Switches_on ; For receptacles
 :parameters(?o - obj ?r - immobileR ?l - location)
 :precondition(and(human_switched_off ?o ?r ?l)
                  (human_near ?r ?l)
                  (not(heavy_obj_in_human_hand))
                  (not(human_hands_occupied_wo))
                  (not(human_hands_occupied_wr))
                  (not(human_switched_on ?o ?r ?l)))
 :effect(and(not(human_switched_off ?o ?r ?l))
                (human_switched_on ?o ?r ?l)
                (increase (total-cost) 15))
)


(:action Human_Switches_off ; For receptacles
 :parameters(?o - obj ?r - immobileR ?l - location)
 :precondition(and(human_switched_on ?o ?r ?l)
                  (human_near ?r ?l)
                  (not(human_switched_off ?o ?r ?l)))
 :effect(and(human_switched_off ?o ?r ?l)
            (not(human_switched_on ?o ?r ?l))
            (increase (total-cost) 15)
        )
)



(:action human_Switch_on ;For big objects
 :parameters(?o - obj ?l - location)
 :precondition(and(human_switch_off ?o)
                  (B_obj_at ?o ?l)
                  (Human_at ?l)
                  (not(human_hands_occupied_wo))
                  (not(human_hands_occupied_wr))
                  (not(human_switch_on ?o ?l)))
 :effect(and(not(human_switch_off ?o))
                (human_switch_on ?o ?l)
                (increase (total-cost) 10))
)


(:action human_Switch_off ;For big objects
 :parameters(?o - obj ?l - location)
 :precondition(and(human_switch_on ?o ?l)
                  (not(human_hands_occupied_wo))
                  (not(human_hands_occupied_wr))
                  (B_obj_at ?o ?l)
                  (Human_at ?l)
                  (not(human_switch_off ?o)))
 :effect(and(human_switch_off ?o)
            (not(human_switch_on ?o ?l))
            (increase (total-cost) 10)
 
        )
)


; Moving around objects and receptacles


;HUMAN
(:action Human_Picks 
 :parameters(?o - obj ?r - immobileR ?l - location)
 :precondition(and(human_near ?r ?l)
                  (stuff_at ?o ?r ?l)
                  (not(In_human_hand ?o))
                  (not(heavy_obj_in_human_hand))
                  )
 :effect(and(In_human_hand ?o)
            (human_hands_occupied_wo)
            (not(stuff_at ?o ?r ?l))
            (increase (total-cost) 20)
        )
)


;HUMAN
(:action Human_PutDowns 
 :parameters (?o - obj ?r -  immobileR ?l - location)
 :precondition (and(human_near ?r ?l)
                   (In_human_hand ?o)
                   (not_burner ?r)
                )
 :effect (and(not(In_human_hand ?o))
             (not(human_hands_occupied_wo))
             (stuff_at ?o ?r ?l)
             (increase (total-cost) 20))  
) 


;HUMAN
(:action Human_Picks_S 
 :parameters(?o - sensitive_obj ?r - immobileR ?l - location)
 :precondition(and(human_near ?r ?l)
                  (stuff_at ?o ?r ?l)
                  (not(heavy_obj_in_human_hand))
                  (not(In_human_hand ?o)))
 :effect(and(In_human_hand ?o)
            (human_hands_occupied_wo)
            (not(stuff_at ?o ?r ?l))
            (increase (total-cost) 15)
        )
)


;HUMAN
(:action Human_PutDowns_S
 :parameters (?o - sensitive_obj ?r -  immobileR ?l - location)
 :precondition (and(human_near ?r ?l)
                   (In_human_hand ?o)
                )
 :effect (and(not(In_human_hand ?o))
             (not(human_hands_occupied_wo))
             (stuff_at ?o ?r ?l)
             (increase (total-cost) 15))  
) 


(:action human_PutDown
 :parameters (?o - obj ?r1 - mobileR ?r2 - immobileR ?l)
 :precondition(and(human_near ?r2 ?l)
                  (receptacle_at ?r1 ?r2 ?l)
                  (or(In_human_hand ?o)(InHumanHand ?o))
                  (not(item_in ?o ?r1 ?r2 ?l))
 )
 :effect(and(item_in ?o ?r1 ?r2 ?l)
            (not(In_human_hand ?o))
            (not(human_hands_occupied_wo))
            (receptacle_at ?o ?r2 ?l)
            (increase (total-cost) 20)
)
)



(:action human_PutDown_s
 :parameters (?o - sensitive_obj ?r1 - mobileR ?r2 - immobileR ?l)
 :precondition(and(human_near ?r2 ?l)
                  (receptacle_at ?r1 ?r2 ?l)
                  (In_human_hand ?o)
                  (not(item_in ?o ?r1 ?r2 ?l))
 )
 :effect(and(item_in ?o ?r1 ?r2 ?l)
            (not(human_hands_occupied_wo))
            (not(In_human_hand ?o))
            (increase (total-cost) 2)
)
)



;HUMAN
(:action Human_PicksUp_Object ;For big objects
 :parameters(?o - obj  ?l - location)
 :precondition(and(Human_at ?l)
                  (B_obj_at ?o ?l)
                  (not(human_hands_occupied_wo))
                  (not(human_hands_occupied_wr))
                  (not(heavy_obj_in_human_hand))
                  (not(In_human_handB ?o)))
 :effect(and(In_human_handB ?o)
            (not(B_obj_at ?o ?l))
            (heavy_obj_in_human_hand)
            (increase (total-cost) 20)
        )
)


;HUMAN
(:action Human_PutsDown_Object ;For big objects
 :parameters (?o - obj  ?l - location)
 :precondition (and(Human_at ?l)
                   (In_human_handB ?o)
                   (not(B_obj_at ?o ?l))
                )
 :effect (and(not(In_human_handB ?o))
             (B_obj_at ?o ?l)
             (not(heavy_obj_in_human_hand))
             (increase (total-cost) 20))  
) 



(:action Open                    
 :parameters (?r - immobileR ?l - location)
 :precondition(and(human_near ?r ?l)
                  (not(open ?r ?l)))
 :effect(and(open ?r ?l)
            (increase (total-cost) 10)
        ) 
)


;HUMAN
(:action Human_PicksUp_FReceptacle
 :parameters(?f - fragile_receptacle ?r - immobileR ?l - location)
 :precondition(and(human_near ?r ?l)
                  (receptacle_at ?f ?r ?l)
                  (not(heavy_obj_in_human_hand))
                  (not(InHumanHand ?f)))
 :effect(and(InHumanHand ?f)
            (not(receptacle_at ?f ?r ?l))
            (human_hands_occupied_wr)
            (increase (total-cost) 5)
        )
)


;HUMAN
(:action Human_PutsDown_FReceptacle 
 :parameters (?f - fragile_receptacle ?r - immobileR ?l - location)
 :precondition (and(InHumanHand ?f)
                   (human_near ?r ?l)
                ;    (not(receptacle_at ?f ?r ?l))
                   (not(human_near stove_burner_1 kitchen))(not(human_near stove_burner_2 kitchen))(not(human_near stove_burner_3 kitchen))(not(human_near stove_burner_4 kitchen))
                )
 :effect (and(not(InHumanHand ?f))
             (receptacle_at ?f ?r ?l)
             (not(human_hands_occupied_wr))
             (increase (total-cost) 5))
) 


;HUMAN
(:action Human_PicksUp_Receptacle
 :parameters(?f - mobileR ?r - immobileR ?l - location)
 :precondition(and(human_near ?r ?l)
                  (receptacle_at ?f ?r ?l)
                  (not(heavy_obj_in_human_hand))
                  (not(InHumanHand ?f)))
 :effect(and(InHumanHand ?f)
            (human_hands_occupied_wr)
            (not(receptacle_at ?f ?r ?l))
            (increase (total-cost) 20)
        )
)


;HUMAN
(:action Human_PutsDown_Receptacle 
 :parameters (?f - mobileR ?r - immobileR ?l - location)
 :precondition (and(InHumanHand ?f)
                   (human_near ?r ?l)
                   (not_fragile ?f)
                ;    (not(receptacle_at ?f ?r ?l))
                )
 :effect (and(not(InHumanHand ?f))
             (not(human_hands_occupied_wr))
             (receptacle_at ?f ?r ?l)
             (increase (total-cost) 20))
) 


;; High level tasks


;HUMAN
(:action human_cleans 
 :parameters (?o1 - obj)
 :precondition (and(not(human_hands_occupied_wo))
                   (not(human_hands_occupied_wr))
                   (not(heavy_obj_in_human_hand))
                   (human_near sink kitchen)
                   (stuff_at ?o1 sink Kitchen)
                   (not(In_human_hand ?o1))
                   (not(cleaned ?o1))
                   (human_switched_on Faucet sink Kitchen)
                )

 :effect(and
            (when(and(not(InHumanhand plate_1))
            (not(InHumanhand plate_2))
            (not(InHumanhand glass_1))
            (not(InHumanhand glass_2))
            (not(InHumanhand bowl_1))
            (not(InHumanhand bowl_2)))
            (cleaned ?o1))
            (increase (total-cost) 75))
)


;HUMAN
(:action human_slice 
 :parameters(?o1 ?o2 - slicable)
 :precondition (and (not(human_hands_occupied_wo))
                    (not(human_hands_occupied_wr))
                    (human_near countertop kitchen)
                    (not(heavy_obj_in_human_hand))
                    (stuff_at ?o1 countertop Kitchen)
                    (not(In_human_hand ?o1))
                    (not(In_human_hand ?o2))
                    (not(sliced ?o2))
                    (cleaned ?o1)
                    (equal ?o1 ?o2)
                )
 :effect (and
            (when(and(not(InHumanhand plate_1))
            (not(InHumanhand plate_2))
            (not(InHumanhand glass_1))
            (not(InHumanhand glass_2))
            (not(InHumanhand bowl_1))
            (not(InHumanhand bowl_2)))
            (sliced ?o2))
             (stuff_at ?o2 countertop Kitchen)
             (increase (total-cost) 30)
         )                 
)




(:action Make_Fruit_Salad
 :parameters (?o1 ?o2 ?o3 ?o4 - fruit)
 :precondition(and(not(human_hands_occupied_wo))
                  (not(human_hands_occupied_wr))
                  (not(heavy_obj_in_human_hand))
                  (sliced ?o1)(sliced ?o2)(sliced ?o3)
                  (human_near countertop kitchen)
                  (item_in ?o1 plate_1 countertop kitchen)
                  (item_in ?o2 plate_1 countertop kitchen)
                  (item_in ?o3 plate_1 countertop kitchen)
                  (salad ?o4)
                  (not(salad_prepared ?o1 ?o2 ?o3))
                  (not(prepared ?o4))
              )
 :effect(and
            (when(and(not(InHumanhand plate_1))
            (not(InHumanhand plate_2))
            (not(InHumanhand glass_1))
            (not(InHumanhand glass_2))
            (not(InHumanhand bowl_1))
            (not(InHumanhand bowl_2)))
            (salad_prepared ?o1 ?o2 ?o3))
            (prepared ?o4)
            (stuff_at ?o4 countertop kitchen)
            (increase (total-cost) 80)
        )  
)



;HUMAN
(:action human_cooks  ; Add cooking waste
 :parameters( ?o1 ?o3 - food)
 :precondition (and (not(human_hands_occupied_wo))
                    (not(human_hands_occupied_wr))
                    (cleaned ?o1)
                    (not(heavy_obj_in_human_hand))
                    (human_near stove_burner_1 kitchen)
                    (item_in ?o1 metal_pot stove_burner_1 kitchen)
                    (equal ?o1 ?o3)
                    (not(cooked ?o3))
                    (human_switched_on burner stove_burner_1 Kitchen) 
                )
 :effect (and 
             (when(and(not(InHumanhand plate_1))
                      (not(InHumanhand plate_2))
                      (not(InHumanhand glass_1))
                      (not(InHumanhand glass_2))
                      (not(InHumanhand bowl_1))
                      (not(InHumanhand bowl_2)))
                      (cooked ?o3))
             (stuff_at ?o3 stove_burner_1 Kitchen)
             (increase (total-cost) 50)
         )                 
)



(:action Human_boils
 :parameters (?o1 ?o2 - ToBoil)
 :precondition(and(not(human_hands_occupied_wo))
                  (not(human_hands_occupied_wr))
                  (item_in ?o1 metal_pot stove_burner_2 kitchen)
                  (not(heavy_obj_in_human_hand))
                  (human_near stove_burner_2 kitchen)
                  (equal ?o1 ?o2)
                  (human_switched_on burner stove_burner_2 Kitchen) 
                  (not(boiled ?o2))
              )
 :effect(and
            (when(and(not(InHumanhand plate_1))
                      (not(InHumanhand plate_2))
                      (not(InHumanhand glass_1))
                      (not(InHumanhand glass_2))
                      (not(InHumanhand bowl_1))
                      (not(InHumanhand bowl_2)))
                      (boiled ?o2))
            (stuff_at ?o2 stove_burner_2 kitchen)
            (increase (total-cost) 30)
        )
)



(:action Human_Roast
 :parameters (?o1 ?o2 - ToRoast)
 :precondition(and(not(human_hands_occupied_wo))
                  (not(human_hands_occupied_wr))
                  (item_in ?o1 pan_1 stove_burner_3 kitchen)
                  (not(heavy_obj_in_human_hand))
                  (equal ?o1 ?o2)
                  (human_near stove_burner_3 kitchen)
                  (human_switched_on burner stove_burner_3 Kitchen) 
                  (not(roasted ?o2))
              )
 :effect(and
            (when(and(not(InHumanhand plate_1))
                      (not(InHumanhand plate_2))
                      (not(InHumanhand glass_1))
                      (not(InHumanhand glass_2))
                      (not(InHumanhand bowl_1))
                      (not(InHumanhand bowl_2)))
                      (roasted ?o2))
            (stuff_at ?o2 stove_burner_3 kitchen)
            (increase (total-cost) 25)
        )
)



(:action Human_Prepare_eggs
 :parameters (?o1 ?o2 - ToFry)
 :precondition(and(not(human_hands_occupied_wr))
                  (not(human_hands_occupied_wo))
                  (item_in ?o1 pan_2 stove_burner_4 kitchen)
                  (not(heavy_obj_in_human_hand))
                  (equal ?o1 ?o2)
                  (human_near stove_burner_4 kitchen)
                  (human_switched_on burner stove_burner_4 Kitchen) 
                  (not(egg_prepared ?o2))
              )
 :effect(and
            (when(and(not(InHumanhand plate_1))
                      (not(InHumanhand plate_2))
                      (not(InHumanhand glass_1))
                      (not(InHumanhand glass_2))
                      (not(InHumanhand bowl_1))
                      (not(InHumanhand bowl_2)))
                      (egg_prepared ?o2))
            (stuff_at ?o2 stove_burner_4 kitchen)
            (increase (total-cost) 25)
        )  
)


; PREPARING PIZZA


;HUMAN
(:action Human_prepares_pizza_base
 :parameters()
 :precondition(and(not(human_hands_occupied_wo))
                  (not(human_hands_occupied_wr))
                  (item_in pizza_base pan_1 countertop kitchen)
                  (not(heavy_obj_in_human_hand))
                  (stuff_at Veggy countertop kitchen)
                  (human_near countertop kitchen)
                  (stuff_at Sauce countertop kitchen)
                  (not(pizza_base_prepared)))
 :effect(and
            (when(and(not(InHumanhand plate_1))
                      (not(InHumanhand plate_2))
                      (not(InHumanhand glass_1))
                      (not(InHumanhand glass_2))
                      (not(InHumanhand bowl_1))
                      (not(InHumanhand bowl_2)))
                      (pizza_base_prepared))
            (stuff_at prepared_pizza_base countertop kitchen)
            (increase(total-cost)20))

)


;HUMAN
(:action Human_bake_pizza
 :parameters()
 :precondition(and(not(human_hands_occupied_wo))
                  (not(human_hands_occupied_wr))
                  (human_near oven Kitchen)
                  (not(heavy_obj_in_human_hand))
                  (pizza_base_prepared)
                  (stuff_at prepared_pizza_base oven Kitchen)
                  (not(pizza_baked))
                  )
 :effect(and
            (when(and(not(InHumanhand plate_1))
                      (not(InHumanhand plate_2))
                      (not(InHumanhand glass_1))
                      (not(InHumanhand glass_2))
                      (not(InHumanhand bowl_1))
                      (not(InHumanhand bowl_2)))
                      (pizza_baked))
            (stuff_at baked_pizza oven Kitchen)
            (increase(total-cost)60)
            )
 )


;HUMAN
(:action Human_serves_pizza
 :parameters(?r1 - fragile_receptacle ?r2 - immobileR ?l - location)
 :precondition(and (pizza_baked)
                   (human_near ?r2 ?l)
                   (not(heavy_obj_in_human_hand))
                   (receptacle_at ?r1 ?r2 ?l)
                   (stuff_at baked_pizza ?r2 ?l)
                   (not(In_human_hand baked_pizza))
                   (not(pizza_served ?r1 ?r2 ?l)))
 :effect(and(pizza_served ?r1 ?r2 ?l)
            (stuff_at remaining_pizza ?r2 ?l)
            (increase(total-cost)40)
 )
)


;HUMAN
(:action human_serves_food 
 :parameters(?o1 - obj ?r1 - fragile_receptacle ?r2 - immobileR ?l - location)
 :precondition(and
                  (or(cooked ?o1)(boiled ?o1)(roasted ?o1)(egg_prepared ?o1))
                  (human_near ?r2 ?l)
                  (not(heavy_obj_in_human_hand))
                  (receptacle_at ?r1 ?r2 ?l)
                  (stuff_at ?o1 ?r2 ?l)
                  (not(In_human_hand ?o1))
                  (not(food_served ?o1 ?r1 ?r2 ?l))
              )
 :effect(and(food_served ?o1 ?r1 ?r2 ?l)
            (stuff_at remaining_food ?r2 ?l)
            (stuff_at dirtydishes ?r2 ?l)
            (increase (total-cost) 40)
        )
)



;HUMAN
(:action human_serves_fruit 
 :parameters (?o1 - fruit ?r1 - fragile_receptacle ?r2 - immobileR ?l - location )
 :precondition(and
                  (or(sliced ?o1)(prepared ?o1))
                  (human_near ?r2 ?l)
                  (not(heavy_obj_in_human_hand))
                  (receptacle_at ?r1 ?r2 ?l)
                  (stuff_at ?o1 ?r2 ?l) 
                  (not(In_human_hand ?o1))
                  (not(fruit_served ?o1 ?r1 ?r2 ?l))
              )
 :effect(and(fruit_served ?o1 ?r1 ?r2 ?l)
            (stuff_at Remaining_fruit ?r2 ?l)
            (stuff_at dirtydishes ?r2 ?l)
            (increase (total-cost) 40)
        )
)


;HUMAN
(:action human_serves_vegetable 
 :parameters (?o1 - vegetable ?r1 - fragile_receptacle ?r2 - immobileR ?l - location )
 :precondition(and
                  (cleaned ?o1)
                  (cooked ?o1)
                  (human_near ?r2 ?l)
                  (receptacle_at ?r1 ?r2 ?l)
                  (not(heavy_obj_in_human_hand))
                  (stuff_at ?o1 ?r2 ?l) 
                  (not(In_human_hand ?o1))
                  (not(veggy_served ?o1 ?r2 ?r2 ?l))
              )
 :effect(and(veggy_served ?o1 ?r1 ?r2 ?l)
            (stuff_at Remaining_veggy ?r2 ?l)
            (stuff_at dirtydishes ?r2 ?l)
            (increase (total-cost) 40)
        )
)


(:action BakeACake 
 :parameters(?o1 ?o3 - tobake)
 :precondition (and (human_near oven Kitchen)
                    (not(human_hands_occupied_wo))
                    (not(human_hands_occupied_wr))
                    (not(heavy_obj_in_human_hand))
                    (stuff_at ?o1 oven Kitchen)
                    (not(baked ?o3))
                    (human_switched_on oven_switch oven Kitchen)
                    (equal ?o1 ?o3)   
                )
 :effect (and(baked ?o3)
             (stuff_at ?o3 oven Kitchen)
             (increase (total-cost) 90)
             
         )                 
)


(:action human_serves_baked 
 :parameters(?o1 - tobake ?r1 - fragile_receptacle ?r2 - immobileR ?l - location )
 :precondition(and
                  (baked ?o1)
                  (human_near ?r2 ?l)
                  (receptacle_at ?r1 ?r2 ?l)
                  (not(heavy_obj_in_human_hand))
                  (stuff_at ?o1 ?r2 ?l)
                  (not(In_human_hand ?o1))
                  (human_near ?r2 ?l)
                  (not(baked_served ?o1 ?r1 ?r2 ?l))
             )
 :effect(and(baked_served ?o1 ?r1 ?r2 ?l)
            (stuff_at Remaining_baked ?r2 ?l)
            (stuff_at dirtydishes ?r2 ?l)
            (increase (total-cost) 20)
        )
)


;HUMAN
(:action human_serves_Drink 
 :parameters (?o - drink ?r1 - fragile_receptacle ?r2 - immobileR ?l3 - location)
 :precondition(and
                  (human_near ?r2 ?l3)
                  (receptacle_at ?r1 ?r2 ?l3) 
                  (not(heavy_obj_in_human_hand))
                  (stuff_at ?o ?r2 ?l3)
                  (not(served_drink ?o ?r1 ?r2 ?l3))
            ) 
 :effect(and(served_drink ?o ?r1 ?r2 ?l3)
            (increase (total-cost) 10)
        )
)



;HUMAN
(:action remaining_food_cleaned
 :parameters (?o - obj)
 :precondition(and
                  (stuff_at ?o dustbin_1 Kitchen)
                  (not(cleaned_remaining_food ?o))
              )
 :effect(and(cleaned_remaining_food ?o)
            (increase (total-cost) 15))
)




;HUMAN
(:action human_washingDishes
 :parameters()
 :precondition(and
          (not(human_hands_occupied_wo))
          (not(human_hands_occupied_wr))
          (human_near sink Kitchen)
          (not(heavy_obj_in_human_hand))
          (stuff_at Dirtydishes sink Kitchen)
          (human_switched_on faucet sink Kitchen)
          (not(dishes_cleaned))
 ) 
 :effect(and(dishes_cleaned)
            (stuff_at cleaned_dishes sink Kitchen)
            (increase (total-cost) 10)
            )
)



(:action human_Extinguish_Fire ;For fire extingusiher
 :parameters (?l - location)
 :precondition (and(B_obj_at extinguisher ?l)
                   (human_at ?l)
                   (human_Switch_on extinguisher ?l)
                   (not(FireExtinguished ?l)
               ))
 :effect(and(FireExtinguished ?l)(increase (total-cost) 70))
)


(:action Human_WashingClothes
 :parameters()
 :precondition(and
                  (Human_near washingmachine Bathroom)
                  (stuff_at Clothes washingmachine Bathroom)
                  (human_switched_on washingmachine_Switch washingmachine Bathroom)
                  (not(washed_Clothes))
                  (not(heavy_obj_in_human_hand))
 ) 
 :effect(and(washed_clothes)
            (stuff_at Cleaned_clothes washingmachine Bathroom)
            (increase (total-cost) 60)
 ) 
)


(:action Human_IronClothes
 :parameters()
 :precondition(and(not(human_hands_occupied_wo))
                  (not(human_hands_occupied_wr))
                  (washed_clothes)
                  (human_near ironing_board LivingRoom)
                  (stuff_at Cleaned_clothes ironing_board LivingRoom)
                  (not(Ironedclothes))
                  (not(heavy_obj_in_human_hand))
 ) 
 :effect(and(Ironedclothes)
            (stuff_at Ironed_clothes ironing_board LivingRoom)
            (increase(total-cost)50)
 )
 ) 



(:action Human_FoldClothes
 :parameters()
 :precondition(and(Ironedclothes)
                  (not(human_hands_occupied_wo))
                  (not(human_hands_occupied_wr))
                  (human_near ironing_board LivingRoom)
                  (stuff_at Ironed_Clothes ironing_board LivingRoom)
                  (not(clothes_folded))
                  (not(heavy_obj_in_human_hand))
 )
 :effect(and(clothes_folded)
            (stuff_at folded_clothes ironing_board LivingRoom)
            (increase(total-cost)50)
 )
)



(:action Laundry_Done 
 :parameters()
 :precondition(and(stuff_at folded_clothes Closet LivingRoom)
                  (not(laundrydone))
 ) 
 :effect(and(laundrydone)(increase (total-cost) 10))
)



(:action human_holds_VC_hose  ;For vacuum cleaner
 :parameters(?l - location)
 :precondition(and(Human_at ?l)
                  (human_switch_off vacuum_cleaner)
                  (B_obj_at vacuum_cleaner ?l)
                  (not(heavy_obj_in_human_hand))
 )
 :effect(and(human_hold vacuum_cleaner ?l)
            (heavy_obj_in_human_hand)
            (increase(total-cost)10))
)


(:action human_starts_cleaning_  ;Vacuum cleaning
:parameters (?l - location)
:precondition(and
                 (not(room_cleaned ?l))
                 (human_hold vacuum_cleaner ?l)
                 (human_switch_on vacuum_cleaner ?l)
             ) 
:effect(and(room_cleaned ?l)
           (increase (total-cost) 50)
           (not(heavy_obj_in_human_hand))
       )
)



(:action Human_cleans_electronics
 :parameters (?o - obj ?l - location)
 :precondition(and(human_at ?l)
                  (In_human_handB DustingCloth)
                  (not(electronics_cleaned ?o ?l))
              )
 :effect(and(electronics_cleaned ?o ?l)
            (increase (total-cost) 20)
            )
)



(:action all_electronic_item_cleaned 
 :parameters ()
 :precondition (and(electronics_cleaned TV livingroom)
                   (electronics_cleaned MusicPlayer livingroom)
                   (electronics_cleaned Computer LivingRoom)
                   (not(electronic_items_Cleaned))
               ) 
 :effect(electronic_items_Cleaned)
)



(:action house_cleaned  ;Vacuum cleaning
 :parameters()
 :precondition(and(not(all_rooms_cleaned))
                  (room_cleaned Kitchen)
                  (room_cleaned Bathroom)
                  (room_cleaned livingroom)
                  (human_switch_off vacuum_cleaner)
              )
 :effect(and(all_rooms_cleaned)
        )
)


(:action office_table_ready
 :parameters()
 :precondition(and(receptacle_cleaned working_table livingRoom)
                  (human_switched_on Laptop_Switch working_table livingRoom)
                  (not(office_ready))
                  (In_human_handB Dustingcloth)

 )
 :effect(office_ready)
)


(:action Human_cleans_receptacle
 :parameters (?o - receptacle ?l - location)
 :precondition(and(human_near ?o ?l)
                  (In_human_handB DustingCloth)
                  (not(receptacle_cleaned ?o ?l))
              )
 :effect(and(receptacle_cleaned ?o ?l)
            (increase (total-cost) 25)
            )
)



(:action prepare_office_bag
 :parameters(?o1 ?o2 ?o3 - obj) 
 :precondition(and(item_in ?o1 office_bag working_table
                  livingRoom)
                  (item_in ?o2 office_bag working_table livingroom)
                  (item_in ?o3 office_bag working_table livingRoom)
                  (not(bag_prepared ?o1 ?o2 ?o3))
 )
 :effect(and(bag_prepared ?o1 ?o2 ?o3))
           )
 
 


(:action clothes_prepared
 :parameters(?o - obj ?r - immobileR ?l - location)
 :precondition(and(stuff_at ?o ?r ?l)
                  (not(prepared_clothes ?o ?r ?l))
 )
 :effect(and(prepared_clothes ?o ?r ?l)(increase (total-cost) 10))
)





(:action attached_for_charging
 :parameters(?o - obj)
 :precondition(and(stuff_at ?o working_table   livingRoom)
                  (not(charged ?o))
 )
 :effect(and(charged ?o)(increase (total-cost) 5))
)



(:action human_provides_medicine
 :parameters(?r - immobileR ?l - location)
 :precondition(and(human_near ?r ?l)
                  (human_near ?r ?l)
                  (In_human_hand Medicines)
                  (not(medicines_provided_at ?r ?l))          
 )
 :effect(and(medicines_provided_at ?r ?l)(increase (total-cost) 5))
)



(:action party_starts
 :parameters(?o - tobake)
 :precondition(and(human_switch_on Color_lights livingRoom)
                  (human_near working_table livingRoom)
                  (baked_served ?o plate_1 working_table   livingRoom)
                  (human_switch_on MusicPlayer livingRoom)

)
 :effect(and(party_at livingRoom))
)
 



)