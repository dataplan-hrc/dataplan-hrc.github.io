import json
import os 
import subprocess
import shutil


def txt_to_json(file_path):
    
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    init_states = {f"init_{i+1}": line for i, line in enumerate(lines)}
    
    json_string = json.dumps(init_states, indent=4)
    
    with open('init_states.json', 'w') as json_file:
        json_file.write(json_string)



def json_to_list(path):

    list = []
    with open(path, 'r') as g:
        g_data = json.load(g)
    
    for g in g_data.values():
        list.append(f"{g}")
    
    return list



def create_pddl_problem_file(domain_name, objects, init_states, goal_states, file_name):

    init_states_str = '\n'.join(init_states)
    goal_states_str = (goal_states)


    problem_template = f"""
(define (problem HRI_prob)

(:domain {domain_name})

(:objects
{objects}
)

(:init
{init_states_str}
)


(:goal
  (and
  {goal_states_str}
  )
) 
(:metric minimize (total-cost))
)
                      """
    with open(file_name, 'w') as file:
        file.write(problem_template.strip())




def gen_problem_file(init, goal):

  g_states = json_to_list(goal)

  txt_to_json(init)

  i_states = json_to_list('init_states.json')

  domain_name = "HRI_dom"

  objects = """ 
      Apple sliced_Apple Avocado sliced_Avocado fruit_salad Banana sliced_Banana - fruit
          
      pasta Cooked_pasta cereal Cooked_cereal - food

      egg omelette scrambled_egg - Tofry

      raw_egg boiled_egg rice cooked_rice lentil cooked_lentil soup prepared_soup - ToBoil

      chicken roasted_chicken bread roasted_sandwich - Toroast

      potato Veggie Mashed_potato - vegetable
          
      wine milk water yogurt juice sweet_juice coke energy_drink - drink
          
      Cellphone cup Casual_clothes office_clothes Gym_clothes chips - obj

      Laptop - sensitive_obj
          
      mold cake - tobake
  """

  for i , g in enumerate(g_states):
    create_pddl_problem_file(domain_name, objects, i_states, g, f'problem_{i+1}.pddl')




def reset_init():
    original_file_path = 'original_init.txt'
    new_file_path = 'init.txt'


    with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
        content = original_file.read()
        new_file.write(content)



def reset_goal(goal):

    if goal=='goals/H4_goal_1.json':

        original_file_path = 'goals/H4_goal_1_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)

    if goal=='goals/H4_goal_2.json':

        original_file_path = 'goals/H4_goal_2_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)

    if goal=='goals/H4_goal_3.json':

        original_file_path = 'goals/H4_goal_3_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)

    if goal=='goals/H4_goal_4.json':

        original_file_path = 'goals/H4_goal_4_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)

    if goal=='goals/H4_goal_5.json':

        original_file_path = 'goals/H4_goal_5_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)


    if goal=='goals/H4_goal_6.json':

        original_file_path = 'goals/H4_goal_6_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)


    if goal=='goals/H4_goal_7.json':

        original_file_path = 'goals/H4_goal_7_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)


    if goal=='goals/H4_goal_8.json':

        original_file_path = 'goals/H4_goal_8_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)


    if goal=='goals/H4_goal_9.json':

        original_file_path = 'goals/H4_goal_9_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)

    if goal=='goals/H4_goal_10.json':

        original_file_path = 'goals/H4_goal_10_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)

    if goal=='goals/H4_goal_11.json':

        original_file_path = 'goals/H4_goal_11_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)

    if goal=='goals/H4_goal_12.json':

        original_file_path = 'goals/H4_goal_12_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)


    if goal=='goals/H4_goal_13.json':

        original_file_path = 'goals/H4_goal_13_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)

    if goal=='goals/H4_goal_14.json':

        original_file_path = 'goals/H4_goal_14_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)


    if goal=='goals/H4_goal_15.json':

        original_file_path = 'goals/H4_goal_15_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)



    if goal=='goals/H4_goal_16.json':

        original_file_path = 'goals/H4_goal_16_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)



    if goal=='goals/H4_goal_17.json':

        original_file_path = 'goals/H4_goal_17_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)



    if goal=='goals/H4_goal_18.json':

        original_file_path = 'goals/H4_goal_18_original.json'
        new_file_path = goal

        with open(original_file_path, 'r') as original_file, open(new_file_path, 'w') as new_file:
            content = original_file.read()
            new_file.write(content)





import subprocess
import os
import shutil

fd_path = os.path.expanduser("~/Desktop/0_my_research/0_code_ubuntu/0_cooking_place/fast-downward-23.06/fast-downward.py")

def run_planner(n):

    """This part runs the planner and saves the plans"""
    
    try:

            if n==0: # at t=0

                goal_dir = "H4_plans"
                os.makedirs(goal_dir, exist_ok=True)

                output = subprocess.run([ fd_path, "--alias", "lama", "--search-time-limit", "90", "--plan-file", f"{goal_dir}/plan_.txt", "0_domain.pddl", "problem_1.pddl"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


            elif n==4: # Human_corrects_himself

                human_corrects = "human_corrects"
                os.makedirs(human_corrects, exist_ok=True)

                output = subprocess.run([ fd_path, "--alias", "lama", "--search-time-limit", "30", "--plan-file", f"{human_corrects}/plan_.txt", "human_domain.pddl", "problem_1.pddl"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            elif n==1: # correction stage

                noise_dir = "H4_noise"
                os.makedirs(noise_dir, exist_ok=True)

                output = subprocess.run([ fd_path, "--alias", "lama", "--search-time-limit", "90", "--plan-file", f"{noise_dir}/plan_.txt", "0_domain.pddl", "problem_1.pddl"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            elif n==2: # human noisy goals

                final_dir = "H4_final"
                os.makedirs(final_dir, exist_ok=True)

                output = subprocess.run([ fd_path, "--alias", "lama", "--search-time-limit", "45", "--plan-file", f"{final_dir}/plan_.txt", "0_domain.pddl", "problem_1.pddl"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            elif n==3: # final stage

                human_dir = "Human_noise"
                os.makedirs(human_dir, exist_ok=True)

                output = subprocess.run([ fd_path, "--alias", "lama", "--search-time-limit", "90", "--plan-file", f"{human_dir}/plan_.txt", "human_domain.pddl", "problem_1.pddl"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            elif n==5: # H4_42

                shivam = "H4_42"
                os.makedirs(shivam, exist_ok=True)

                output = subprocess.run([ fd_path, "--alias", "lama", "--search-time-limit", "30", "--plan-file", f"{shivam}/plan_.txt", "0_domain.pddl", "problem_1.pddl"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            else:
                 print("try again")
                 

            stdout_output = output.stdout.decode()
            stderr_output = output.stderr.decode()

    except subprocess.CalledProcessError as e: #return_code 23 - time limit reached

            stdout_output = e.stdout.decode() if e.stdout else ""
            stderr_output = e.stderr.decode() if e.stderr else ""
            
            if e.returncode==30:
                print(f"major error occured")






def clear_pickput(pick_put):

    while True:

        def find_count(pick_put):
            count = []
            q = 0

            for p in pick_put:
                s=0
                for pp in pick_put:
                    if p[0]==pp[0] and p[1]==pp[1]:
                        s+=1
                count.append(s)

            for i in range(len(count)):
                if count[i]>1:
                    q+=1
                    break

            return count, q

        count, q = find_count(pick_put)

        for i in range(len(count)):
            if count[i]>1:
                pick_put.pop(i)
                break

        count, q = find_count(pick_put)

        if q<1:
            break
    
    return pick_put






        
def extraction(directory, file_name):

    move = [] 
    pick_put = []

    with open(f'{directory}/{file_name}', 'r') as file:
            content = file.readlines()
            modified_content = [i.replace('(', '').replace(')', '').split() for i in content]
            move = [j for j in modified_content if j[0]=='agent_moves_br' or j[0]=='human_moves_br']
            move = move[::-1]
            pick_put = [j for j in modified_content if j[0]=='agent_putdowns' or j[0]=='human_putdowns' or j[0]=='human_putdowns_s'or j[0]=='agent_putsdown_object'or j[0]=='human_putsdown_object'or j[0]=='human_putsdown_freceptacle'or j[0]=='human_putsdown_receptacle'or j[0]=='agent_putsdown_receptacle'or j[0]=='human_putdown' or j[0]=='human_putdown_s' or j[0]=='agent_putdown']

            human_ps = [j for j in modified_content if 
                        j[0]=='human_picks_s'or
                        j[0]=='human_picks' or
                        j[0]=='human_putdowns'or
                        j[0]=='human_putdowns_s'or
                        j[0]=='human_putdown'or
                        j[0]=='human_putdown_s'
                        ]
            human_ps_obj = [o[1] for o in human_ps]
            human_ps_obj = list(set(human_ps_obj))

            
            human_pbo = [j for j in modified_content if 
                        j[0]=='human_picksup_object'or
                        j[0]=='human_putsdown_object']
            human_pbo_obj = [o[1] for o in human_pbo]
            human_pbo_obj = list(set(human_pbo_obj))

            human_pr = [j for j in modified_content if 
                        j[0]=='human_picksup_freceptacle'or
                        j[0]=='human_picksup_receptacle' or
                        j[0]=='human_putsdown_freceptacle'or
                        j[0]=='human_putsdown_receptacle']
            human_pr_obj = [o[1] for o in human_pr]
            human_pr_obj = list(set(human_pr_obj))



            agent_ps = [j for j in modified_content if 
                        j[0]=='agent_pickup'or
                        j[0]=='agent_putdowns' or
                        j[0]=='agent_putdown'
                        ]
            agent_ps_obj = [o[1] for o in agent_ps]
            agent_ps_obj = list(set(agent_ps_obj))

            
            agent_pbo = [j for j in modified_content if 
                        j[0]=='agent_picksup_object'or
                        j[0]=='agent_putsdown_object']
            agent_pbo_obj = [o[1] for o in agent_pbo]
            agent_pbo_obj = list(set(agent_pbo_obj))

            agent_pr = [j for j in modified_content if 
                        j[0]=='agent_picksup_receptacle' or
                        j[0]=='agent_putsdown_receptacle']
            agent_pr_obj = [o[1] for o in agent_pr]
            agent_pr_obj = list(set(agent_pr_obj))
            

            misc = [j for j in modified_content if
                        j[0]=='agent_cleans'or      
                        j[0]=='human_cleans'or 
                        j[0]=='agent_slice'or
                        j[0]=='human_slice'or
                        j[0]=='make_fruit_salad'or
                        j[0]=='human_cooks'or
                        j[0]=='agent_cooks'or
                        j[0]=='bakeacake'or
                        j[0]=='agent_bake_pizza'or
                        j[0]=='human_bake_pizza'or
                        j[0]=='agent_prepares_pizza_base'or
                        j[0]=='human_prepares_pizza_base'or
                        j[0]=='agent_boils'or
                        j[0]=='human_boils'or
                        j[0]=='agent_roast'or
                        j[0]=='human_roast'or
                        j[0]=='human_prepare_eggs'or
                        j[0]=='agent_prepare_eggs'or
                        j[0]=='agent_bake_pizza'or
                        j[0]=='human_bake_pizza'or
                        j[0]=='agent_washingdishes'or
                        j[0]=='human_washingdishes'or
                        j[0]=='agent_washingclothes'or
                        j[0]=='human_washingclothes'or
                        j[0]=='agent_ironclothes'or
                        j[0]=='human_ironclothes'or
                        j[0]=='agent_foldclothes'or
                        j[0]=='human_foldclothes'or
                        j[0]=='laundry_done'or
                        j[0]=='agent_holds_vc_hose'or
                        j[0]=='human_holds_vc_hose'or
                        j[0]=='agent_starts_cleaning_'or
                        j[0]=='human_starts_cleaning_'or
                        j[0]=='agent_passes_to_human'or
                        j[0]=='agent_cleans_electronics'or
                        j[0]=='human_cleans_electronics'or
                        j[0]=='all_electronic_item_cleaned'or
                        j[0]=='house_cleaned'or
                        j[0]=='office_table_ready'or
                        j[0]=='agent_cleans_recepetacle'or
                        j[0]=='human_cleans_receptacle'or
                        j[0]=='prepare_office_bag'or
                        j[0]=='attached_for_charging'or
                        j[0]=='remaining_food_cleaned'or
                        j[0]=='clothes_prepared'or
                        j[0]=='agent_provides_'or
                        j[0]=='party_starts'or
                        j[0]=='agent_extinguish_fire'or
                        j[0]=='human_extinguish_fire'or
                        j[0]=='human_switches_on'or
                        j[0]=='human_switch_on'or
                        j[0]=='agent_switches_on'or
                        j[0]=='agent_switch_on'or
                        j[0]=='human_serves_drink'or
                        j[0]=='agent_serves_drink'or
                        j[0]=='agent_serves_baked'or
                        j[0]=='agent_serves_food'or
                        j[0]=='human_serves_food'
                        ]
      

    def adding_misc_actions(misc):
            
            preconditions_met = []

            with open('init.txt', 'r+') as d:
                lines = d.readlines()

            for i in misc:
                        
                        if i[0]=='agent_serves_food':
                            lines.append(f"(food_served {i[1]} {i[2]} {i[3]} {i[4]})\n")                                  
                            preconditions_met.append(f"food_served {i[1]} {i[2]} {i[3]} {i[4]}")


                        if i[0]=='human_serves_food':
                            lines.append(f"(food_served {i[1]} {i[2]} {i[3]} {i[4]})\n")                             
                            preconditions_met.append(f"food_served {i[1]} {i[2]} {i[3]} {i[4]}")
                                                           
                        
                        if i[0]=='agent_serves_baked':
                            lines.append(f"(baked_served {i[1]} {i[2]} {i[3]} {i[4]})\n")                            
                            preconditions_met.append(f"baked_served {i[1]} {i[2]} {i[3]} {i[4]}")
                                    
                        if  i[0]=='agent_cleans': 
                            lines.append(f"(cleaned {i[-1]})\n")
                            preconditions_met.append(f"cleaned {i[-1]}") 

                        elif  i[0]=='human_cleans': 
                            lines.append(f"(cleaned {i[-1]})\n")
                            preconditions_met.append(f"cleaned {i[-1]}") 

                        elif  i[0]=='agent_slice':
                            lines.append(f"(sliced {i[-1]})\n")
                            lines.append(f"(stuff_at {i[-1]} countertop kitchen)\n")
                            preconditions_met.append(f"sliced {i[-1]}") 
                            
                        elif  i[0]=='human_slice':
                            lines.append(f"(sliced {i[-1]})\n")
                            lines.append(f"(stuff_at {i[-1]} countertop kitchen)\n")
                            preconditions_met.append(f"sliced {i[-1]}") 

                        elif  i[0]=='make_fruit_salad': #changed
                            lines.append(f"(salad_prepared {i[2]} {i[3]} {i[4]})\n")
                            lines.append(f"(prepared {i[5]})\n")
                            lines.append(f"(stuff_at {i[5]} countertop kitchen)\n")
                            preconditions_met.append(f"salad_prepared {i[2]} {i[3]} {i[4]}") 

                        elif  i[0]=='human_cooks':
                            lines.append(f"(cooked {i[-1]})\n")
                            lines.append(f"(stuff_at {i[-1]} stove_burner_1 kitchen)\n")
                            preconditions_met.append(f"cooked {i[-1]}") 

                        elif  i[0]=='agent_cooks':
                            lines.append(f"(cooked {i[-1]})\n")
                            lines.append(f"(stuff_at {i[-1]} stove_burner_1 kitchen)\n")
                            preconditions_met.append(f"cooked {i[-1]}") 

                        elif  i[0]=='bakeacake':
                            lines.append(f"(baked {i[-1]})\n")
                            lines.append(f"(stuff_at {i[-1]} oven kitchen)\n")
                            preconditions_met.append(f"baked {i[-1]}") 

                        elif  i[0]=='agent_bake_pizza':
                            lines.append("(pizza_baked)\n")
                            lines.append("(stuff_at baked_pizza oven kitchen)\n")
                            preconditions_met.append("pizza_baked") 
                            
                        elif  i[0]=='human_bake_pizza':
                            lines.append("(pizza_baked)\n")
                            lines.append("(stuff_at baked_pizza oven kitchen)\n")
                            preconditions_met.append("pizza_baked") 

                        elif  i[0]=='agent_prepares_pizza_base':
                            lines.append("(pizza_base_prepared)\n")
                            lines.append("(stuff_at prepared_pizza_base countertop kitchen)\n")
                            preconditions_met.append("pizza_base_prepared") 

                        elif  i[0]=='human_prepares_pizza_base':
                            lines.append("(pizza_base_prepared)\n")
                            lines.append("(stuff_at prepared_pizza_base countertop kitchen)\n")
                            preconditions_met.append("pizza_base_prepared") 

                        elif  i[0]=='agent_boils':
                            lines.append(f"(boiled {i[-1]})\n")
                            lines.append(f"(stuff_at {i[-1]} stove_burner_2 kitchen)\n")
                            preconditions_met.append(f"boiled {i[-1]}") 

                        elif  i[0]=='human_boils':
                            lines.append(f"(boiled {i[-1]})\n")
                            lines.append(f"(stuff_at {i[-1]} stove_burner_2 kitchen)\n")
                            preconditions_met.append(f"boiled {i[-1]}") 

                        elif  i[0]=='agent_roast':
                            lines.append(f"(roasted {i[-1]})\n")
                            lines.append(f"(stuff_at {i[-1]} stove_burner_3 kitchen)\n")
                            preconditions_met.append(f"roasted {i[-1]}") 

                        elif  i[0]=='human_roast':
                            lines.append(f"(roasted {i[-1]})\n")
                            lines.append(f"(stuff_at {i[-1]} stove_burner_3 kitchen)\n")
                            preconditions_met.append(f"roasted {i[-1]}") 

                        elif  i[0]=='human_prepare_eggs':
                            lines.append(f"(egg_prepared {i[-1]})\n")
                            lines.append(f"(stuff_at {i[-1]} stove_burner_4 kitchen)\n")
                            preconditions_met.append(f"egg_prepared {i[-1]}") 

                        elif  i[0]=='agent_prepare_eggs':
                            lines.append(f"(egg_prepared {i[-1]})\n")
                            lines.append(f"(stuff_at {i[-1]} stove_burner_4 kitchen)\n")
                            preconditions_met.append(f"egg_prepared {i[-1]}") 



                        elif i[0]=='agent_washingdishes':
                            lines.append("(dishes_cleaned)\n")
                            lines.append("(stuff_at cleaned_dishes sink kitchen)\n")
                            preconditions_met.append("dishes_cleaned") 

                        elif  i[0]=='human_washingdishes':
                            lines.append("(dishes_cleaned)\n")
                            lines.append("(stuff_at cleaned_dishes sink kitchen)\n")
                            preconditions_met.append("dishes_cleaned") 

                        elif i[0]=='agent_extinguish_fire':
                            lines.append(f"(fireextinguished {i[-1]})\n")
                            preconditions_met.append(f"fireextinguished {i[-1]}")

                        elif i[0]=='human_extinguish_fire':
                            lines.append(f"(fireextinguished {i[-1]})\n")
                            preconditions_met.append(f"fireextinguished {i[-1]}")

                        elif  i[0]=='agent_washingclothes':
                            lines.append("(washed_clothes)\n")
                            lines.append("(stuff_at cleaned_clothes washingmachine bathroom)\n")
                            preconditions_met.append("washed_clothes") 

                        elif  i[0]=='human_washingclothes':
                            lines.append("(washed_clothes)\n")
                            lines.append("(stuff_at cleaned_clothes washingmachine bathroom)\n")
                            preconditions_met.append("washed_clothes") 

                        elif  i[0]=='agent_ironclothes':
                            lines.append("(ironedclothes)\n")
                            lines.append("(stuff_at ironedclothes ironing_board livingroom)\n")
                            preconditions_met.append("ironedclothes") 

                        elif  i[0]=='human_ironclothes':
                            lines.append("(ironedclothes)\n")
                            lines.append("(stuff_at ironedclothes ironing_board livingroom)\n")
                            preconditions_met.append("ironedclothes") 

                        elif  i[0]=='agent_foldclothes':
                            lines.append("(clothes_folded)\n")
                            lines.append("(stuff_at folded_clothes ironing_board livingroom)\n")
                            preconditions_met.append("clothes_folded") 

                        elif  i[0]=='human_foldclothes':
                            lines.append("(clothes_folded)\n")
                            lines.append("(stuff_at folded_clothes ironing_board livingroom)\n")
                            preconditions_met.append("clothes_folded") 

                        elif  i[0]=='laundry_done':
                            lines.append("(laundrydone)\n")
                            preconditions_met.append("laundrydone") 

                        elif  i[0]=='agent_holds_vc_hose':
                            lines.append(f"(agent_hold vacuum_cleaner {i[-1]})\n")
                            preconditions_met.append(f"agent_hold vacuum_cleaner {i[-1]}") 

                        elif  i[0]=='human_holds_vc_hose':
                            lines.append(f"(agent_hold vacuum_cleaner {i[-1]})\n")
                            preconditions_met.append(f"agent_hold vacuum_cleaner {i[-1]}") 

                        elif  i[0]=='agent_starts_cleaning_':
                            lines.append(f"(room_cleaned {i[-1]})\n")
                            preconditions_met.append(f"room_cleaned {i[-1]}") 

                        elif  i[0]=='human_starts_cleaning_':
                            lines.append(f"(room_cleaned {i[-1]})\n")
                            preconditions_met.append(f"room_cleaned {i[-1]}") 

                        elif  i[0]=='agent_passes_to_human':
                            lines.append(f"(in_human_hands {i[1]} {i[-1]})\n")
                            lines.append(f"(in_human_handB {i[1]})\n")
                            lines.append(f"(in_human_hand {i[1]})\n")
                            

                        elif  i[0]=='agent_cleans_electronics':
                            lines.append(f"(electronics_cleaned {i[-2]} {i[-1]})\n")
                            preconditions_met.append(f"electronics_cleaned {i[-2]} {i[-1]}") 
                            
                        elif  i[0]=='human_cleans_electronics':
                            lines.append(f"(electronics_cleaned {i[-2]} {i[-1]})\n")
                            preconditions_met.append(f"electronics_cleaned {i[-2]} {i[-1]}") 

                        elif  i[0]=='all_electronic_item_cleaned':
                            lines.append("(electronic_items_cleaned)\n")
                            preconditions_met.append("electronic_items_cleaned") 

                        elif  i[0]=='house_cleaned':
                            lines.append("(all_rooms_cleaned)\n")
                            preconditions_met.append("all_rooms_cleaned") 

                        elif  i[0]=='office_table_ready':
                            lines.append("(office_ready)\n")
                            preconditions_met.append("office_ready") 

                        elif  i[0]=='agent_cleans_recepetacle':
                            lines.append(f"(receptacle_cleaned {i[-2]} {i[-1]})\n")
                            preconditions_met.append(f"receptacle_cleaned {i[-2]} {i[-1]}") 

                        elif  i[0]=='human_cleans_receptacle':
                            lines.append(f"(receptacle_cleaned {i[-2]} {i[-1]})\n")
                            preconditions_met.append(f"receptacle_cleaned {i[-2]} {i[-1]}") 

                        elif  i[0]=='prepare_office_bag':
                            lines.append(f"(bag_prepared {i[-3]} {i[-2]} {i[-1]})\n")
                            preconditions_met.append(f"bag_prepared {i[-3]} {i[-2]} {i[-1]}") 

                        elif  i[0]=='attached_for_charging':
                            lines.append(f"(charged {i[-1]})\n")
                            preconditions_met.append(f"charged {i[-1]}") 
                            
                        elif  i[0]=='remaining_food_cleaned':
                            lines.append(f"(cleaned_remaining food {i[-1]})\n")
                            preconditions_met.append(f"cleaned_remaining food {i[-1]}") 

                        elif  i[0]=='clothes_prepared':
                            lines.append(f"(prepared_clothes {i[-3]} {i[-2]} {i[-1]})\n")
                            preconditions_met.append(f"prepared_clothes {i[-3]} {i[-2]} {i[-1]}") 

                        elif  i[0]=='agent_provides_':
                            lines.append(f"(provided_at medicines {i[-2]} {i[-1]})\n")
                            preconditions_met.append(f"provided_at medicines {i[-2]} {i[-1]}") 
                            
                        # elif i[0]=='party_starts':
                        #     lines.append("(party_at livingroom)\n")
                        #     preconditions_met.append("party_at livingroom") 

                        
                        elif i[0]=='agent_serves_drink': #changed
                             lines.append(f"(served_drink {i[1]} {i[2]} {i[3]} {i[4]})\n")
                             preconditions_met.append(f"served_drink {i[1]} {i[2]} {i[3]} {i[4]}")

                        elif i[0]=='human_serves_drink': #changed
                             preconditions_met.append(f"served_drink {i[1]} {i[2]} {i[3]} {i[4]}")
                             lines.append(f"(served_drink {i[1]} {i[2]} {i[3]} {i[4]})\n")

                        elif  i[0]=='human_switches_on':
                            lines.append(f"(human_switched_on {i[-3]} {i[-2]} {i[-1]})\n")
                            lines.append(f"(agent_switched_on {i[-3]} {i[-2]} {i[-1]})\n")

                        elif  i[0]=='human_switch_on':
                            lines.append(f"(human_switch_on {i[-2]} {i[-1]})\n")
                            lines.append(f"(agent_switch_on {i[-2]} {i[-1]})\n")

                        elif  i[0]=='agent_switches_on':
                            lines.append(f"(human_switched_on {i[-3]} {i[-2]} {i[-1]})\n")
                            lines.append(f"(agent_switched_on {i[-3]} {i[-2]} {i[-1]})\n")

                        elif  i[0]=='agent_switch_on':
                            lines.append(f"(human_switch_on {i[-2]} {i[-1]})\n")
                            lines.append(f"(agent_switch_on {i[-2]} {i[-1]})\n")

                            
            for o in human_ps_obj:
                                s = 0
                                r=0
                                for p in human_ps:
                                    if p[0]=='human_putdowns' and p[1]==o:
                                        r+=1
                                       
                                        remove_1 = f"(in_human_hand {o})"
                                        remove_2 = '(human_hands_occupied_wo)'

                                        for k, l in enumerate(lines):
                                            if l.strip() == remove_1.strip():
                                                lines[k] = ''
                                            elif l.strip() == remove_2.strip():
                                                lines[k] = ''                                            
                                        

                                    elif p[0]=='human_putdowns_s' and p[1]==o:
                                        r+=1
                                        remove_1 = f"(in_human_hand {o})"
                                        remove_2 = '(human_hands_occupied_wo)'

                                        for k, l in enumerate(lines):
                                            if l.strip() == remove_1.strip():
                                                lines[k] = ''
                                            elif l.strip() == remove_2.strip():
                                                lines[k] = ''                                            
                                       

                                    elif p[0]=='human_putdown_s' and p[1]==o:
                                        r+=1
                                        remove_1 = f"(in_human_hand {o})"
                                        remove_2 = '(human_hands_occupied_wo)'

                                        for k, l in enumerate(lines):
                                            if l.strip() == remove_1.strip():
                                                lines[k] = ''
                                            elif l.strip() == remove_2.strip():
                                                lines[k] = ''                                            
                                       

                                    elif p[0]=='human_putdown' and p[1]==o:
                                        r+=1
                                        remove_1 = f"(in_human_hand {o})"
                                        remove_2 = '(human_hands_occupied_wo)'

                                        for k, l in enumerate(lines):
                                            if l.strip() == remove_1.strip():
                                                lines[k] = ''
                                            elif l.strip() == remove_2.strip():
                                                lines[k] = ''                                            
                                       
                                                                            
                                for p in human_ps:
                                    if o==p[1]:
                                        s+=1
                                if s%2!=0 and r==0:
                                    lines.append(f"(in_human_hand {o})\n")
                                    lines.append("(human_hands_occupied_wo)\n")



            for o in human_pbo_obj:
                                s = 0
                                r=0
                                for p in human_pbo:
                                    if p[0]=='human_putsdown_object' and p[1]==o:
                                        r+=1
                                        remove_1 = f"(in_human_handB {o})"
                                        remove_2 = "(heavy_obj_in_human_hand)"

                                        for k, l in enumerate(lines):
                                            if l.strip() == remove_1.strip():
                                                lines[k] = ''
                                            elif l.strip() == remove_2.strip():
                                                lines[k] = ''                                            
                                       
                                for p in human_pbo:
                                    if o==p[1]:
                                        s+=1
                                if s%2!=0 and r==0:
                                    lines.append(f"(in_human_handB {o})\n")
                                    lines.append("(heavy_obj_in_human_hand)\n")


            for o in human_pr_obj:
                                s = 0
                                r=0
                                for p in human_pr:
                                    if p[0]=='human_putsdown_freceptacle' and p[1]==o:
                                        r+=1
                                        remove_1 = f"(inhumanhand {o})"
                                        remove_2 = "(human_hands_occupied_wr)"

                                        for k, l in enumerate(lines):
                                            if l.strip() == remove_1.strip():
                                                lines[k] = ''
                                            elif l.strip() == remove_2.strip():
                                                lines[k] = ''                 

                                    elif p[0]=='human_putsdown_receptacle' and p[1]==o:
                                        r+=1

                                        remove_1 = f"(inhumanhand {o})"
                                        remove_2 = "(human_hands_occupied_wr)"

                                        for k, l in enumerate(lines):
                                            if l.strip() == remove_1.strip():
                                                lines[k] = ''
                                            elif l.strip() == remove_2.strip():
                                                lines[k] = ''     

                                for p in human_pr:
                                    if o==p[1]:
                                        s+=1
                                if s%2!=0 and r==0:
                                    lines.append(f"(inhumanhand {o})\n")  
                                    lines.append("(human_hands_occupied_wr)\n")    
                            

            for o in agent_ps_obj:
                                s = 0
                                r=0
                                for p in agent_ps:
                                    if p[0]=='agent_putdowns' and p[1]==o:
                                        r+=1

                                        remove_1 = f"(in_agent_hand {o})\n"
                                        remove_2 = "(agent_hands_occupied_wo)\n"

                                        for k, l in enumerate(lines):
                                            if l.strip() == remove_1.strip():
                                                lines[k] = ''
                                            elif l.strip() == remove_2.strip():
                                                lines[k] = ''     

                                    elif p[0]=='agent_putdown' and p[1]==o:
                                        r+=1 
                                        remove_1 = f"(in_agent_hand {o})\n"
                                        remove_2 = "(agent_hands_occupied_wo)\n"

                                        for k, l in enumerate(lines):
                                            if l.strip() == remove_1.strip():
                                                lines[k] = ''
                                            elif l.strip() == remove_2.strip():
                                                lines[k] = ''  


                                for p in agent_ps:
                                    if o==p[1]:
                                        s+=1
                                if s%2!=0 and r==0:
                                    lines.append(f"(in_agent_hand {o})\n")
                                    lines.append("(agent_hands_occupied_wo)\n")


            for o in agent_pbo_obj:
                                s = 0
                                r=0
                                for p in agent_pbo:
                                    if p[0]=='agent_putsdown_object' and p[1]==o:
                                        r+=1
                                        remove_1 = f"(in_agent_handB {o})\n"
                                        remove_2 = "(heavy_obj_in_agent_hand)\n"

                                        for k, l in enumerate(lines):
                                            if l.strip() == remove_1.strip():
                                                lines[k] = ''
                                            elif l.strip() == remove_2.strip():
                                                lines[k] = ''  

                                for p in agent_pbo:
                                    if o==p[1]:
                                        s+=1
                                if s%2!=0 and r==0:
                                    lines.append(f"(in_agent_handB {o})\n")
                                    lines.append("(heavy_obj_in_agent_hand)\n")


            for o in agent_pr_obj:
                                s = 0
                                r=0
                                for p in agent_pr:
                                    if p[0]=='agent_putsdown_receptacle' and p[1]==o:
                                        r+=1
                                        remove_1 = f"(inagenthand {o})\n"
                                        remove_2 = "(agent_hands_occupied_wr)\n"

                                        for k, l in enumerate(lines):
                                            if l.strip() == remove_1.strip():
                                                lines[k] = ''
                                            elif l.strip() == remove_2.strip():
                                                lines[k] = ''  
                                        
                                for p in agent_pr:
                                    if o==p[1]:
                                        s+=1
                                if s%2!=0 and r==0:
                                    lines.append(f"(inagenthand {o})\n")  
                                    lines.append("(agent_hands_occupied_wr)\n")  

            with open('init.txt', 'w') as file:
                file.writelines(lines)

            return preconditions_met


    preconditions_met = adding_misc_actions(misc)

                
    def mov(move):
            hpos = []
            apos = []
            for i in move:
                if i[0]=='human_moves_br':
                        hpos.append(i)
                        break
            for j in move:
                if j[0]=='agent_moves_br':
                        apos.append(j)
                        break

            if not(len(hpos))==0:
                h_pos = (f"human_at {hpos[0][-1]}")
                h_rpos = (f"human_near {hpos[0][-3]} {hpos[0][-1]}")
            else:
                h_pos = ""
                h_rpos = ""
            
            if not(len(apos))==0:
                a_pos = (f"agent_at {apos[0][-1]}")
                a_rpos = (f"agent_near {apos[0][-3]} {apos[0][-1]}")
            else:
                a_pos = ""
                a_rpos = ""
            
            posn = []
            posn.append(h_pos)
            posn.append(h_rpos)
            posn.append(a_pos)
            posn.append(a_rpos)

            return posn

    def pipu(pick_put):
    
            ao_p = []
            ho_p = []
            hso_p= []
            abo_p = []
            hbo_p = []
            hfr_p = []
            hr_p = []
            ar_p = []
            h_pd = []
            h_pds = []
            a_pd = []



            for i in pick_put:
                if i[0]=='agent_putdowns':
                        ao_p.append(i)
            for j in pick_put:
                if j[0]=='human_putdowns':
                        ho_p.append(j)
            for k in pick_put:
                if k[0]=='human_putdowns_s':
                        hso_p.append(k)
            for o in pick_put:
                if o[0]=='agent_putsdown_object':
                        abo_p.append(o)
            for p in pick_put:
                if p[0]=='human_putsdown_object':
                        hbo_p.append(p)
            for q in pick_put:
                if q[0]=='human_putsdown_freceptacle':
                        hfr_p.append(q)
            for r in pick_put:
                if r[0]=='human_putsdown_receptacle':
                        hr_p.append(r)
            for s in pick_put:
                if s[0]=='agent_putsdown_receptacle':
                        ar_p.append(s)
            for s in pick_put:
                if s[0]=='agent_putdown':
                        a_pd.append(s)
            for s in pick_put:
                if s[0]=='human_putdown':
                        h_pd.append(s)
            for s in pick_put:
                if s[0]=='human_putdown_s':
                        h_pds.append(s)

            stuff_posn = []
            

            if not(len(a_pd))==0:
                 for i in a_pd:
                      stuff_posn.append(f"item_in {i[1]} {i[2]} {i[3]} {i[4]}")

            if not(len(h_pd))==0:
                 for i in h_pd:
                      stuff_posn.append(f"item_in {i[1]} {i[2]} {i[3]} {i[4]}")

            if not(len(h_pds))==0:
                 for i in h_pds:
                      stuff_posn.append(f"item_in {i[1]} {i[2]} {i[3]} {i[4]}")

            
            if not(len(ao_p))==0:
                for i in ao_p:
                        stuff_posn.append(f"stuff_at {i[-3]} {i[-2]} {i[-1]}")
                        preconditions_met.append(f"stuff_at {i[-3]} {i[-2]} {i[-1]}")

            if not(len(ho_p))==0:
                for i in ho_p:
                        stuff_posn.append(f"stuff_at {i[-3]} {i[-2]} {i[-1]}")
                        preconditions_met.append(f"stuff_at {i[-3]} {i[-2]} {i[-1]}")

            if not(len(hso_p))==0:
                for i in hso_p:
                        stuff_posn.append(f"stuff_at {i[-3]} {i[-2]} {i[-1]}")
                        preconditions_met.append(f"stuff_at {i[-3]} {i[-2]} {i[-1]}")

            if not(len(abo_p))==0:
                for i in abo_p:
                        stuff_posn.append(f"b_obj_at {i[-2]} {i[-1]}")
                        preconditions_met.append(f"b_obj_at {i[-2]} {i[-1]}")

            if not(len(hbo_p))==0:
                for i in hbo_p:
                        stuff_posn.append(f"b_obj_at {i[-2]} {i[-1]}")
                        preconditions_met.append(f"b_obj_at {i[-2]} {i[-1]}")

            if not(len(hfr_p))==0:
                for i in hfr_p:
                        stuff_posn.append(f"receptacle_at {i[-3]} {i[-2]} {i[-1]}") 
                        preconditions_met.append(f"receptacle_at {i[-3]} {i[-2]} {i[-1]}")

            if not(len(hr_p))==0:
                for i in hr_p:
                        stuff_posn.append(f"receptacle_at {i[-3]} {i[-2]} {i[-1]}") 
                        preconditions_met.append(f"receptacle_at {i[-3]} {i[-2]} {i[-1]}")

            if not(len(ar_p))==0:
                for i in ar_p:
                        stuff_posn.append(f"receptacle_at {i[-3]} {i[-2]} {i[-1]}") 
                        preconditions_met.append(f"receptacle_at {i[-3]} {i[-2]} {i[-1]}")
            

            return stuff_posn


    posn = mov(move)

    pick_put = clear_pickput(pick_put)
    stuff_posn = pipu(pick_put)

    return posn, stuff_posn, preconditions_met
      




def update_init(posn, stuff_posn):

    with open('init.txt', 'r+') as d:
            lines = d.readlines()
            
            if all(posn):
                for i, line in enumerate(lines):
                        if line.startswith('(human_at'):
                            lines[i] = f"({posn[0]})\n"
                        elif line.startswith('(human_near'):
                            lines[i] = f"({posn[1]})\n"
                        elif line.startswith('(agent_at'):
                            lines[i] = f"({posn[2]})\n"
                        elif line.startswith('(agent_near'):
                            lines[i] = f"({posn[3]})\n"
            
            
            elif (posn[0]=='') and (posn[1]=='') and not(posn[2]=='') and not(posn[3]==''):
                for i, line in enumerate(lines):
                        if line.startswith('(agent_at'):
                            lines[i] = f"({posn[2]})\n"
                        elif line.startswith('(agent_near'):
                            lines[i] = f"({posn[3]})\n"


                
            elif (posn[2]=='') and (posn[3]=='')and not(posn[0]=='') and not(posn[1]==''):
                for i, line in enumerate(lines):
                        if line.startswith('(human_at'):
                            lines[i] = f"({posn[0]})\n"
                        elif line.startswith('(human_near'):
                            lines[i] = f"({posn[1]})\n"



            for i in range(len(stuff_posn)):

                prefix = ' '.join(stuff_posn[i].split()[:2])
                n=0
                for j, line in enumerate(lines):
                        if line.startswith(f'({prefix}'):
                            lines[j] = f"({stuff_posn[i]})\n"
                            n+=1
                
                if n==0:
                
                        lines.append(f"({stuff_posn[i]})\n")


            d.seek(0)
            d.writelines(lines)
            d.truncate()  




import random
import math


def multiple_noise_plan(od, of, q, number_of_noise):

    rack_options = ['plate_1', 'plate_2', 'metal_pot', 'plate_3', 'plate_4', 'plate_5']

    cabinet_options = [ 'cereal', 'mold', 'wine', 'pasta', 'rice', 'soup', 'bread', 'medicines', 'pizza_base', 'lentil', 'chips' ]

    shelf_options = ['pan_1', 'pan_2', 'glass_1', 'glass_2', 'bowl_1', 'bowl_2']

    fridge_options = ['apple', 'banana', 'avocado', 'veggie', 'potato', 'raw_egg', 'egg', 'milk', 'water', 'yogurt', 'juice', 'coke', 'energy_drink', 'veggy', 'sauce', 'sweet_juice']

    closet_options = ['casual_clothes', 'office_clothes', 'gym_clothes'] 

    ppl = []
    recep = ['closet', 'rack', 'cabinet', 'shelf', 'fridge']
    ppl_lines = []
    stuff_already_picked = []
    
    with open(f'{od}/{of}', 'r+') as d:

        lines = d.readlines()

    for k, line in enumerate(lines):
        
        if line.startswith('(human_pick') and lines[k].split()[2] in recep:

            ppl.append(k)
            ppl_lines.append(line)

    for k, line in enumerate(lines):
        
        if line.startswith('(agent_pick') and lines[k].split()[2] in recep:

            ppl.append(k)
            ppl_lines.append(line)


    stuff_already_picked = [l.split()[1] for l in ppl_lines]

    for i in range(len(rack_options) - 1, -1, -1):
        if rack_options[i] in stuff_already_picked:
            rack_options.pop(i)

    for i in range(len(cabinet_options) - 1, -1, -1):
        if cabinet_options[i] in stuff_already_picked:
            cabinet_options.pop(i)

    for i in range(len(shelf_options) - 1, -1, -1):
        if shelf_options[i] in stuff_already_picked:
            shelf_options.pop(i)

    for i in range(len(fridge_options) - 1, -1, -1):
        if fridge_options[i] in stuff_already_picked:
            fridge_options.pop(i)
            
    for i in range(len(closet_options) - 1, -1, -1):
        if closet_options[i] in stuff_already_picked:
            closet_options.pop(i)

   
   # q is the list that contains noisy instances.
   
    for x in range(number_of_noise):
        
        for k, line in enumerate(lines):
                
            if k == q[x]:

                if line.startswith('(human_pick'):
                    
                    a = line.split()

                    if a[2] == 'closet':
                        for i in range(len(closet_options)):
                            if a[1]==closet_options[i] :
                                closet_options.pop(i)
                                break
                        a[1] = random.choice(closet_options)
                        for i in range(len(closet_options)):
                            if a[1]==closet_options[i] :
                                closet_options.pop(i)
                                break
                        lines[k] = ' '.join(a) + '\n'

                    elif a[2] == 'shelf':
                        for i in range(len(shelf_options)):
                            if a[1]==shelf_options[i]:
                                shelf_options.pop(i)
                                break
                        a[1] = random.choice(shelf_options)
                        for i in range(len(shelf_options)):
                            if a[1]==shelf_options[i] :
                                shelf_options.pop(i)
                                break
                        lines[k] = ' '.join(a) + '\n'

                    elif a[2] == 'rack':
                        for i in range(len(rack_options)):
                            if a[1]==rack_options[i]:
                                rack_options.pop(i)
                                break
                        a[1] = random.choice(rack_options)
                        for i in range(len(rack_options)):
                            if a[1]==rack_options[i] :
                                rack_options.pop(i)
                                break
                        lines[k] = ' '.join(a) + '\n'

                    elif a[2] == 'fridge':
                        for i in range(len(fridge_options)):
                            if a[1]==fridge_options[i]:
                                fridge_options.pop(i)
                                break
                        a[1] = random.choice(fridge_options)
                        for i in range(len(fridge_options)):
                            if a[1]==fridge_options[i] :
                                fridge_options.pop(i)
                                break
                        lines[k] = ' '.join(a) + '\n'


                    elif a[2] == 'cabinet':
                        for i in range(len(cabinet_options)):
                            if a[1]==cabinet_options[i]:
                                cabinet_options.pop(i)
                                break
                        a[1] = random.choice(cabinet_options)
                        for i in range(len(cabinet_options)):
                            if a[1]==cabinet_options[i] :
                                cabinet_options.pop(i)
                                break
                        lines[k] = ' '.join(a) + '\n'


                    else:
                        noise = 0


    new_file_path = 'H4_noise/noisy_plan.txt'
    with open(new_file_path, 'w') as new_file:
        new_file.writelines(lines)




import random
import math


def agent_multiple_noise_plan(od, of, q, number_of_noise):

    rack_options = ['plate_1', 'plate_2', 'metal_pot', 'plate_3', 'plate_4', 'plate_5']

    cabinet_options = [ 'cereal', 'mold', 'wine', 'pasta', 'rice', 'soup', 'bread', 'medicines', 'pizza_base', 'lentil', 'chips' ]

    shelf_options = ['pan_1', 'pan_2', 'glass_1', 'glass_2', 'bowl_1', 'bowl_2']

    fridge_options = ['apple', 'banana', 'avocado', 'veggie', 'potato', 'raw_egg', 'egg', 'milk', 'water', 'yogurt', 'juice', 'coke', 'energy_drink', 'veggy', 'sauce', 'sweet_juice']

    closet_options = ['casual_clothes', 'office_clothes', 'gym_clothes'] 

    ppl = []
    recep = ['closet', 'rack', 'cabinet', 'shelf', 'fridge']
    ppl_lines = []
    stuff_already_picked = []
    
    with open(f'{od}/{of}', 'r+') as d:

        lines = d.readlines()

    for k, line in enumerate(lines):
        
        if line.startswith('(human_pick') and lines[k].split()[2] in recep:

            ppl.append(k)
            ppl_lines.append(line)

    for k, line in enumerate(lines):
        
        if line.startswith('(agent_pick') and lines[k].split()[2] in recep:

            ppl.append(k)
            ppl_lines.append(line)


    stuff_already_picked = [l.split()[1] for l in ppl_lines]

    for i in range(len(rack_options) - 1, -1, -1):
        if rack_options[i] in stuff_already_picked:
            rack_options.pop(i)

    for i in range(len(cabinet_options) - 1, -1, -1):
        if cabinet_options[i] in stuff_already_picked:
            cabinet_options.pop(i)

    for i in range(len(shelf_options) - 1, -1, -1):
        if shelf_options[i] in stuff_already_picked:
            shelf_options.pop(i)

    for i in range(len(fridge_options) - 1, -1, -1):
        if fridge_options[i] in stuff_already_picked:
            fridge_options.pop(i)
            
    for i in range(len(closet_options) - 1, -1, -1):
        if closet_options[i] in stuff_already_picked:
            closet_options.pop(i)

   
   # q is the list that contains noisy instances.
   
    for x in range(number_of_noise):
        
        for k, line in enumerate(lines):
                
            if k == q[x]:

                if line.startswith('(agent_pick'):
                    
                    a = line.split()

                    if a[2] == 'closet':
                        for i in range(len(closet_options)):
                            if a[1]==closet_options[i] :
                                closet_options.pop(i)
                                break
                        a[1] = random.choice(closet_options)
                        for i in range(len(closet_options)):
                            if a[1]==closet_options[i] :
                                closet_options.pop(i)
                                break
                        lines[k] = ' '.join(a) + '\n'

                    elif a[2] == 'shelf':
                        for i in range(len(shelf_options)):
                            if a[1]==shelf_options[i]:
                                shelf_options.pop(i)
                                break
                        a[1] = random.choice(shelf_options)
                        for i in range(len(shelf_options)):
                            if a[1]==shelf_options[i] :
                                shelf_options.pop(i)
                                break
                        lines[k] = ' '.join(a) + '\n'

                    elif a[2] == 'rack':
                        for i in range(len(rack_options)):
                            if a[1]==rack_options[i]:
                                rack_options.pop(i)
                                break
                        a[1] = random.choice(rack_options)
                        for i in range(len(rack_options)):
                            if a[1]==rack_options[i] :
                                rack_options.pop(i)
                                break
                        lines[k] = ' '.join(a) + '\n'

                    elif a[2] == 'fridge':
                        for i in range(len(fridge_options)):
                            if a[1]==fridge_options[i]:
                                fridge_options.pop(i)
                                break
                        a[1] = random.choice(fridge_options)
                        for i in range(len(fridge_options)):
                            if a[1]==fridge_options[i] :
                                fridge_options.pop(i)
                                break
                        lines[k] = ' '.join(a) + '\n'


                    elif a[2] == 'cabinet':
                        for i in range(len(cabinet_options)):
                            if a[1]==cabinet_options[i]:
                                cabinet_options.pop(i)
                                break
                        a[1] = random.choice(cabinet_options)
                        for i in range(len(cabinet_options)):
                            if a[1]==cabinet_options[i] :
                                cabinet_options.pop(i)
                                break
                        lines[k] = ' '.join(a) + '\n'


                    else:
                        noise = 0


    new_file_path = 'H4_noise/agent_noisy_plan.txt'
    with open(new_file_path, 'w') as new_file:
        new_file.writelines(lines)







""" Finding the plan before noise """
def plan_before_noise (od, of):  #modified

    noisy_action = []
    noise_actual = []

    with open(f'{od}/{of}', 'r') as file1, open('H4_noise/noisy_plan.txt', 'r') as file2, open('H4_noise/plan_before_noise.txt', 'w') as target:

        for i, (line1, line2) in enumerate(zip(file1, file2), start=1):
            if line1 == line2:
                target.write(line1)
            elif line1!=line2:
                target.write(line2)
                break


    with open(f'{od}/{of}', 'r') as file1, open('H4_noise/noisy_plan.txt', 'r') as file2:
        for i, (line1, line2) in enumerate(zip(file1, file2), start=1):
            if line1!=line2:
                noisy_action.append(line1)
                noise_actual.append(line2)

    noisy_action = [i.replace('(', '').replace(')', '').split() for i in noisy_action]

    noise_actual = [i.replace('(', '').replace(')', '').split() for i in noise_actual]

    

    return noisy_action, noise_actual



""" Finding the noise goal state """

def noisy_goal(noisy_action, od, of):

    pp = []

    with open(f"{od}/{of}") as file:
        lines = file.readlines()
        for i,l in enumerate(lines, start=1):
            if l.startswith('(agent_pu') or l.startswith('(human_pu'):
                pp.append(l.split())

    pp = [[s.replace('(', '').replace(')', '') for s in sublist] for sublist in pp]
    q = []

    for p in pp:
        if p[1]==noisy_action[0][1]:
            q = p
            break

    if q[0]=='human_putdowns':
        goal = f"(stuff_at {q[1]} {q[2]} {q[3]})"

    elif q[0]=='human_putdowns_s':
        goal = f"(stuff_at {q[1]} {q[2]} {q[3]})"

    elif q[0]=='human_putdown':
        goal=f"(item_in {q[1]} {q[2]} {q[3]} {q[4]})"

    elif q[0]=='human_putdown_s':
        goal=f"(item_in {q[1]} {q[2]} {q[3]} {q[4]})"

    elif q[0]=='human_putsdown_object':
        goal = f"(b_obj_at {q[1]} {q[2]})"

    elif q[0]=='human_putsdown_freceptacle':
        goal = f"(receptacle_at {q[1]} {q[2]} {q[3]})"
        
    elif q[0]=='human_putsdown_receptacle':
        goal = f"(receptacle_at {q[1]} {q[2]} {q[3]})"

    data = {
        "goal_1": f"{goal}"
        }

    filename = 'noise_goal.json'
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    return goal








""" Finding the plan before noise """
def agent_plan_before_noise (od, of):  #modified

    noisy_action = []
    noise_actual = []

    with open(f'{od}/{of}', 'r') as file1, open('H4_noise/agent_noisy_plan.txt', 'r') as file2, open('H4_noise/agent_plan_before_noise.txt', 'w') as target:

        for i, (line1, line2) in enumerate(zip(file1, file2), start=1):
            if line1 == line2:
                target.write(line1)
            elif line1!=line2:
                target.write(line2)
                break


    with open(f'{od}/{of}', 'r') as file1, open('H4_noise/agent_noisy_plan.txt', 'r') as file2:
        for i, (line1, line2) in enumerate(zip(file1, file2), start=1):
            if line1!=line2:
                noisy_action.append(line1)
                noise_actual.append(line2)

    noisy_action = [i.replace('(', '').replace(')', '').split() for i in noisy_action]

    noise_actual = [i.replace('(', '').replace(')', '').split() for i in noise_actual]

    

    return noisy_action, noise_actual



""" Finding the noise goal state """

def agent_noisy_goal(noisy_action, od, of):

    pp = []

    with open(f"{od}/{of}") as file:
        lines = file.readlines()
        for i,l in enumerate(lines, start=1):
            if l.startswith('(agent_pu') or l.startswith('(human_pu'):
                pp.append(l.split())

    pp = [[s.replace('(', '').replace(')', '') for s in sublist] for sublist in pp]
    q = []

    for p in pp:
        if p[1]==noisy_action[0][1]:
            q = p
            break

    if q[0]=='agent_putdowns':
        goal = f"(stuff_at {q[1]} {q[2]} {q[3]})"

    elif q[0]=='agent_putdowns_s':
        goal = f"(stuff_at {q[1]} {q[2]} {q[3]})"

    elif q[0]=='agent_putdown':
        goal=f"(item_in {q[1]} {q[2]} {q[3]} {q[4]})"

    elif q[0]=='agent_putdown_s':
        goal=f"(item_in {q[1]} {q[2]} {q[3]} {q[4]})"

    elif q[0]=='agent_putsdown_object':
        goal = f"(b_obj_at {q[1]} {q[2]})"

    elif q[0]=='agent_putsdown_freceptacle':
        goal = f"(receptacle_at {q[1]} {q[2]} {q[3]})"
        
    elif q[0]=='agent_putsdown_receptacle':
        goal = f"(receptacle_at {q[1]} {q[2]} {q[3]})"

    data = {
        "goal_1": f"{goal}"
        }

    filename = 'agent_noise_goal.json'
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    return goal



def show_differences(od, of):
    
    with open('H4_noise/plan_before_noise.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip('()\n').split() for line in lines]


    mv = [l for l in lines if l[0]=='human_moves_br' or l[0]=='agent_moves_br']

    with open('dur_costs.txt', 'r') as file:
        dlines = file.readlines()
        dlines  = [dlines[i].split() for i in range(len(dlines))]


    disth = []
    dista = []

    for m in range(len(mv)):

        if mv[m][0]=='human_moves_br':
            for i in range(len(dlines)):
                if mv[m][0]=='human_moves_br'and dlines[i][0]=='(=(human_dur':
                    if dlines[i][1]==mv[m][1] and dlines[i][2]==mv[m][2]:
                        disth.append(dlines[i])
        elif mv[m][0]=='agent_moves_br':  
            for i in range(len(dlines)):              
                if mv[m][0]=='agent_moves_br'and dlines[i][0]=='(=(agent_dur':
                    if dlines[i][1]==mv[m][1] and dlines[i][2]==mv[m][2]:
                        dista.append(dlines[i])
        

    sh = 0
    sa = 0

    if len(disth)>0:
        for i in disth:
            sh = sh + int(i[3][1:])

    if len(dista)>0:
        for i in dista:
            sa = sa + int(i[3][1:])

    distance_cost = sh + sa


    msum = 0

    for i in range(len(lines)):
        
        if lines[i][0]=='agent_cleans':
            msum+=25      
        elif lines[i][0]=='human_cleans': 
            msum+=75
        elif lines[i][0]=='agent_slice':
            msum+=15
        elif lines[i][0]=='human_slice':
            msum+=30
        elif lines[i][0]=='make_fruit_salad':
            msum+=80
        elif lines[i][0]=='human_cooks':
            msum+=50
        elif lines[i][0]=='agent_cooks':
            msum+=80
        elif lines[i][0]=='bakeacake':
            msum+=90
        elif lines[i][0]=='agent_bake_pizza':
            msum+=20
        elif lines[i][0]=='human_bake_pizza':
            msum+=60
        elif lines[i][0]=='agent_prepares_pizza_base':
            msum+=60
        elif lines[i][0]=='human_prepares_pizza_base':
            msum+=20
        elif lines[i][0]=='agent_boils':
            msum+=15
        elif lines[i][0]=='human_boils':
            msum+=30
        elif lines[i][0]=='agent_roast':
            msum+=60
        elif lines[i][0]=='human_roast':
            msum+=25
        elif lines[i][0]=='human_prepare_eggs':
            msum+=25
        elif lines[i][0]=='agent_prepare_eggs':
            msum+=80
        elif lines[i][0]=='agent_bake_pizza':
            msum+=20
        elif lines[i][0]=='human_bake_pizza':
            msum+=60
        elif lines[i][0]=='agent_washingdishes':
            msum+=30
        elif lines[i][0]=='human_washingdishes':
            msum+=10
        elif lines[i][0]=='agent_washingclothes':
            msum+=40
        elif lines[i][0]=='human_washingclothes':
            msum+=60
        elif lines[i][0]=='agent_ironclothes':
            msum+=40
        elif lines[i][0]=='human_ironclothes':
            msum+=50
        elif lines[i][0]=='agent_foldclothes':
            msum+=30
        elif lines[i][0]=='human_foldclothes':
            msum+=50
        elif lines[i][0]=='laundry_done':
            msum+=10
        elif lines[i][0]=='agent_holds_vc_hose':
            msum+=10
        elif lines[i][0]=='human_holds_vc_hose':
            msum+=10
        elif lines[i][0]=='agent_starts_cleaning_':
            msum+=45
        elif lines[i][0]=='human_starts_cleaning_':
            msum+=50
        elif lines[i][0]=='agent_passes_to_human':
            msum+=5
        elif lines[i][0]=='agent_cleans_electronics':
            msum+=60
        elif lines[i][0]=='human_cleans_electronics':
            msum+=20
        elif lines[i][0]=='all_electronic_item_cleaned':
            msum+=0
        elif lines[i][0]=='house_cleaned':
            msum+=0
        elif lines[i][0]=='office_table_ready':
            msum+=0
        elif lines[i][0]=='agent_cleans_recepetacle':
            msum+=20
        elif lines[i][0]=='human_cleans_receptacle':
            msum+=25
        elif lines[i][0]=='prepare_office_bag':
            msum+=0
        elif lines[i][0]=='attached_for_charging':
            msum+=5
        elif lines[i][0]=='remaining_food_cleaned':
            msum+=15
        elif lines[i][0]=='clothes_prepared':
            msum+=10
        elif lines[i][0]=='agent_provides_':
            msum+=5
        elif lines[i][0]=='party_starts':
            msum+=0
        elif lines[i][0]=='agent_extinguish_fire':
            msum+=50
        elif lines[i][0]=='human_extinguish_fire':
            msum+=70
        elif lines[i][0]=='human_switches_on':
            msum+=15
        elif lines[i][0]=='agent_switches_on':
            msum+=10
        elif lines[i][0]=='human_switch_on':
            msum+=10
        elif lines[i][0]=='agent_switch_on':
            msum+=10


        elif lines[i][0]=='agent_pickup':
            msum+=20
        elif lines[i][0]=='agent_putdowns':
            msum+=20
        elif lines[i][0]=='human_picks':
            msum+=20
        elif lines[i][0]=='human_putdowns':
            msum+=20
        elif lines[i][0]=='human_picks_s':
            msum+=15
        elif lines[i][0]=='human_putdown_s':
            msum+=15
        elif lines[i][0]=='agent_putdown':
            msum+=10
        elif lines[i][0]=='human_putdown':
            msum+=20
        elif lines[i][0]=='human_putdown_s':
            msum+=2
        elif lines[i][0]=='agent_picksup_object':
            msum+=10
        elif lines[i][0]=='human_picksup_object':
            msum+=20
        elif lines[i][0]=='agent_putsdown_object':
            msum+=10
        elif lines[i][0]=='human_putsdown_object':
            msum+=20
        elif lines[i][0]=='human_picksup_freceptacle':
            msum+=5
        elif lines[i][0]=='human_putsdown_freceptacle':
            msum+=5
        elif lines[i][0]=='human_picksup_receptacle':
            msum+=20
        elif lines[i][0]=='human_putsdown_receptacle':
            msum+=20
        elif lines[i][0]=='agent_picksup_receptacle':
            msum+=10
        elif lines[i][0]=='agent_putsdown_receptacle':
            msum+=10


    cost_before_noise = msum + distance_cost


    directory = 'H4_final'
    file_name = f'plan_.txt.{len(os.listdir(directory))}'

    with open(f'{directory}/{file_name}', 'r') as file:
            lines = file.readlines()

    noise_final_cost = int(lines[-1].split()[3])


    total_noise_cost = cost_before_noise + noise_final_cost
    

    with open(f'{od}/{of}', 'r') as file:
            lines = file.readlines()

    noise_free_cost = int(lines[-1].split()[3])


    print(f"Plan cost with noise: {total_noise_cost}")
    print(f"Plan without noise: {noise_free_cost}")
    print("\n\n")

    return (noise_free_cost, total_noise_cost)



def agent_show_differences(od, of):
    
    with open('H4_noise/agent_plan_before_noise.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip('()\n').split() for line in lines]


    mv = [l for l in lines if l[0]=='human_moves_br' or l[0]=='agent_moves_br']

    with open('dur_costs.txt', 'r') as file:
        dlines = file.readlines()
        dlines  = [dlines[i].split() for i in range(len(dlines))]


    disth = []
    dista = []

    for m in range(len(mv)):

        if mv[m][0]=='human_moves_br':
            for i in range(len(dlines)):
                if mv[m][0]=='human_moves_br'and dlines[i][0]=='(=(human_dur':
                    if dlines[i][1]==mv[m][1] and dlines[i][2]==mv[m][2]:
                        disth.append(dlines[i])
        elif mv[m][0]=='agent_moves_br':  
            for i in range(len(dlines)):              
                if mv[m][0]=='agent_moves_br'and dlines[i][0]=='(=(agent_dur':
                    if dlines[i][1]==mv[m][1] and dlines[i][2]==mv[m][2]:
                        dista.append(dlines[i])
        

    sh = 0
    sa = 0

    if len(disth)>0:
        for i in disth:
            sh = sh + int(i[3][1:])

    if len(dista)>0:
        for i in dista:
            sa = sa + int(i[3][1:])

    distance_cost = sh + sa


    msum = 0

    for i in range(len(lines)):
        
        if lines[i][0]=='agent_cleans':
            msum+=25      
        elif lines[i][0]=='human_cleans': 
            msum+=75
        elif lines[i][0]=='agent_slice':
            msum+=15
        elif lines[i][0]=='human_slice':
            msum+=30
        elif lines[i][0]=='make_fruit_salad':
            msum+=80
        elif lines[i][0]=='human_cooks':
            msum+=50
        elif lines[i][0]=='agent_cooks':
            msum+=80
        elif lines[i][0]=='bakeacake':
            msum+=90
        elif lines[i][0]=='agent_bake_pizza':
            msum+=20
        elif lines[i][0]=='human_bake_pizza':
            msum+=60
        elif lines[i][0]=='agent_prepares_pizza_base':
            msum+=60
        elif lines[i][0]=='human_prepares_pizza_base':
            msum+=20
        elif lines[i][0]=='agent_boils':
            msum+=15
        elif lines[i][0]=='human_boils':
            msum+=30
        elif lines[i][0]=='agent_roast':
            msum+=60
        elif lines[i][0]=='human_roast':
            msum+=25
        elif lines[i][0]=='human_prepare_eggs':
            msum+=25
        elif lines[i][0]=='agent_prepare_eggs':
            msum+=80
        elif lines[i][0]=='agent_bake_pizza':
            msum+=20
        elif lines[i][0]=='human_bake_pizza':
            msum+=60
        elif lines[i][0]=='agent_washingdishes':
            msum+=30
        elif lines[i][0]=='human_washingdishes':
            msum+=10
        elif lines[i][0]=='agent_washingclothes':
            msum+=40
        elif lines[i][0]=='human_washingclothes':
            msum+=60
        elif lines[i][0]=='agent_ironclothes':
            msum+=40
        elif lines[i][0]=='human_ironclothes':
            msum+=50
        elif lines[i][0]=='agent_foldclothes':
            msum+=30
        elif lines[i][0]=='human_foldclothes':
            msum+=50
        elif lines[i][0]=='laundry_done':
            msum+=10
        elif lines[i][0]=='agent_holds_vc_hose':
            msum+=10
        elif lines[i][0]=='human_holds_vc_hose':
            msum+=10
        elif lines[i][0]=='agent_starts_cleaning_':
            msum+=45
        elif lines[i][0]=='human_starts_cleaning_':
            msum+=50
        elif lines[i][0]=='agent_passes_to_human':
            msum+=5
        elif lines[i][0]=='agent_cleans_electronics':
            msum+=60
        elif lines[i][0]=='human_cleans_electronics':
            msum+=20
        elif lines[i][0]=='all_electronic_item_cleaned':
            msum+=0
        elif lines[i][0]=='house_cleaned':
            msum+=0
        elif lines[i][0]=='office_table_ready':
            msum+=0
        elif lines[i][0]=='agent_cleans_recepetacle':
            msum+=20
        elif lines[i][0]=='human_cleans_receptacle':
            msum+=25
        elif lines[i][0]=='prepare_office_bag':
            msum+=0
        elif lines[i][0]=='attached_for_charging':
            msum+=5
        elif lines[i][0]=='remaining_food_cleaned':
            msum+=15
        elif lines[i][0]=='clothes_prepared':
            msum+=10
        elif lines[i][0]=='agent_provides_':
            msum+=5
        elif lines[i][0]=='party_starts':
            msum+=0
        elif lines[i][0]=='agent_extinguish_fire':
            msum+=50
        elif lines[i][0]=='human_extinguish_fire':
            msum+=70
        elif lines[i][0]=='human_switches_on':
            msum+=15
        elif lines[i][0]=='agent_switches_on':
            msum+=10
        elif lines[i][0]=='human_switch_on':
            msum+=10
        elif lines[i][0]=='agent_switch_on':
            msum+=10


        elif lines[i][0]=='agent_pickup':
            msum+=20
        elif lines[i][0]=='agent_putdowns':
            msum+=20
        elif lines[i][0]=='human_picks':
            msum+=20
        elif lines[i][0]=='human_putdowns':
            msum+=20
        elif lines[i][0]=='human_picks_s':
            msum+=15
        elif lines[i][0]=='human_putdown_s':
            msum+=15
        elif lines[i][0]=='agent_putdown':
            msum+=10
        elif lines[i][0]=='human_putdown':
            msum+=20
        elif lines[i][0]=='human_putdown_s':
            msum+=2
        elif lines[i][0]=='agent_picksup_object':
            msum+=10
        elif lines[i][0]=='human_picksup_object':
            msum+=20
        elif lines[i][0]=='agent_putsdown_object':
            msum+=10
        elif lines[i][0]=='human_putsdown_object':
            msum+=20
        elif lines[i][0]=='human_picksup_freceptacle':
            msum+=5
        elif lines[i][0]=='human_putsdown_freceptacle':
            msum+=5
        elif lines[i][0]=='human_picksup_receptacle':
            msum+=20
        elif lines[i][0]=='human_putsdown_receptacle':
            msum+=20
        elif lines[i][0]=='agent_picksup_receptacle':
            msum+=10
        elif lines[i][0]=='agent_putsdown_receptacle':
            msum+=10


    cost_before_noise = msum + distance_cost


    directory = 'H4_final'
    file_name = f'plan_.txt.{len(os.listdir(directory))}'

    with open(f'{directory}/{file_name}', 'r') as file:
            lines = file.readlines()

    noise_final_cost = int(lines[-1].split()[3])



    total_noise_cost = cost_before_noise + noise_final_cost

    with open(f'{od}/{of}', 'r') as file:
            lines = file.readlines()

    noise_free_cost = int(lines[-1].split()[3])


    print(f"Plan cost with noise: {total_noise_cost}")
    print(f"Plan without noise: {noise_free_cost}")
    print("\n\n")

    return (noise_free_cost, total_noise_cost)



def copy_text(first_file, output_file_path):

    with open(output_file_path, 'w') as output_file:
        
                with open(first_file, 'r') as file:
                    content = file.read()
                    
                    output_file.write(content + "\n") 




import json

def append_goal_to_json(goal, new_goal):

    with open(goal, 'r') as json_file:
        data = json.load(json_file)
    
    # Append the new goal to 'goal_1'
    if 'goal_1' in data:
        data['goal_1'] += new_goal
    else:
        data['goal_1'] = new_goal
    
    # Write the updated dictionary back to the JSON file
    with open(goal, 'w') as json_file:
        json.dump(data, json_file, indent=4)




def putdown_goal(noisy_action):

    if noisy_action[0][0]=='human_picks':
        goal = f'(not(in_human_hand {noisy_action[0][1]}))'
       
    elif noisy_action[0][0]=='human_picks_s':
        goal = f'(not(in_human_hand {noisy_action[0][1]}))'
        
    elif noisy_action[0][0]=='human_picksup_object':
        goal = f'(not(in_human_handB {noisy_action[0][1]}))'

    elif noisy_action[0][0]=='human_picksup_freceptacle':
        goal = f'(not(inhumanhand {noisy_action[0][1]}))'

    elif noisy_action[0][0]=='human_picksup_receptacle':
        goal = f'(not(inhumanhand {noisy_action[0][1]}))'

    return goal



def agent_putdown_goal(noisy_action):

    if noisy_action[0][0]=='agent_pickup':
        goal = f'(not(in_agent_hand {noisy_action[0][1]}))'
      
    elif noisy_action[0][0]=='agent_picksup_object':
        goal = f'(not(in_agent_handB {noisy_action[0][1]}))'

    elif noisy_action[0][0]=='agent_picksup_receptacle':
        goal = f'(not(inagenthand {noisy_action[0][1]}))'

    return goal



def finding_preconditions(goal):
    
    import json
    import re

    with open(goal, 'r') as file:
        f = json.load(file)

    goal_states = [i for i in f.values()]

    pattern = r'\([^\)]+\)'
    goal_states = re.findall(pattern, goal_states[0])
    goal_states = [i.replace('(', '').replace(')', '').split() for i in goal_states]

    precondition = []

    for i in goal_states:

        if i[0]=='cleaned':
            precondition.append(f'(stuff_at {i[1]} sink kitchen)')

        elif i[0]=='sliced':
            precondition.append('(human_near countertop kitchen)')
            
        elif i[0]=='salad_prepared': #changed
            precondition.append(f'(sliced {i[2]})')
            precondition.append(f'(sliced {i[3]})')
            precondition.append(f'(sliced {i[4]})')

        elif i[0]=='cooked':
            precondition.append('(human_near stove_burner_1 kitchen)')
            precondition.append('(human_switched_on burner stove_burner_1 kitchen)')

        elif i[0]=='boiled':
            precondition.append('(human_near stove_burner_2 kitchen)')
            precondition.append('(human_switched_on burner stove_burner_2 kitchen)')

        elif i[0]=='roasted':
            precondition.append('(human_near stove_burner_3 kitchen)')
            precondition.append('(human_switched_on burner stove_burner_3 kitchen)')

        elif i[0]=='egg_prepared':
            precondition.append('human_near stove_burner_4 kitchen')
            precondition.append('(human_switched_on burner stove_burner_4 kitchen)')

        elif i[0]=='pizza_base_prepared':
            precondition.append('(stuff_at veggy countertop kitchen)')
            precondition.append('(stuff_at sauce countertop kitchen)')

        elif i[0]=='pizza_baked':
            precondition.append('(stuff_at veggy countertop kitchen)')
            precondition.append('(stuff_at sauce countertop kitchen)')
            precondition.append('(stuff_at prepared_pizza_base oven kitchen)')

        
        elif i[0]=='pizza_served':
            precondition.append('(stuff_at veggy countertop kitchen)')
            precondition.append('(stuff_at sauce countertop kitchen)')
            precondition.append('(stuff_at prepared_pizza_base oven kitchen)')
            precondition.append(f'(receptacle_at {i[1]} {i[2]} {i[3]})')
            precondition.append(f'(stuff_at baked_pizza {i[2]} {i[3]})')

        elif i[0]=='food_served':
            precondition.append(f'(receptacle_at {i[2]} {i[3]} {i[4]})')
            precondition.append(f'(stuff_at {i[1]} {i[3]} {i[4]})')

        elif i[0]=='fruit_served':

            precondition.append(f'(sliced {i[1]})')
            precondition.append(f'(receptacle_at {i[2]} {i[3]} {i[4]})')
            precondition.append(f'(stuff_at {i[1]} {i[3]} {i[4]})')

        elif i[0]=='baked':

            precondition.append('(stuff_at mold oven kitchen)')

        elif i[0]=='served_drink':
            precondition.append(f'(receptacle_at {i[2]} {i[3]} {i[4]})')
            precondition.append(f'(stuff_at {i[1]} {i[3]} {i[4]})')

        elif i[0]=='cleaned_remaining_food':
            precondition.append(f'(stuff_at {i[1]} dustbin_1 kitchen)')

        elif i[0]=='dishes_cleaned':
            precondition.append('(stuff_at dirtydishes sink kitchen)')

        elif i[0]=='fireextinguished':
            precondition.append(f'(b_obj_at extinguisher {i[1]})')

        elif i[0]=='washed_clothes':
            precondition.append('(stuff_at clothes washingmachine bathroom)')

        
        elif i[0]=='ironedclothes':
            precondition.append('(washed_clothes)')
            precondition.append('(stuff_at cleaned_clothes ironing_board livingroom)')

        elif i[0]=='clothes_folded':
            precondition.append('(stuff_at clothes washingmachine bathroom)')
            precondition.append('(washed_clothes)')
            precondition.append('(stuff_at cleaned_clothes ironing_board livingroom)')
            precondition.append('(ironedclothes)')
            precondition.append('(stuff_at ironed_clothes ironing_board livingroom)')

        elif i[0]=='laundrydone':
            precondition.append('(stuff_at clothes washingmachine bathroom)')
            precondition.append('(washed_clothes)')
            precondition.append('(stuff_at cleaned_clothes ironing_board livingroom)')
            precondition.append('(ironedclothes)')
            precondition.append('(stuff_at ironed_clothes ironing_board livingroom)')
            precondition.append('(stuff_at folded_clothes closet livingroom)')

        elif i[0]=='room_cleaned':
            precondition.append(f'(b_obj_at vacuum_cleaner {i[1]})')

        elif i[0]=='office_ready':
            precondition.append('(receptacle_cleaned working_table livingroom)')

        elif i[0]=='bag_prepared':

            precondition.append(f'(item_in {i[1]} office_bag working_table livingroom)')
            precondition.append(f'(item_in {i[2]} office_bag working_table livingroom)')
            precondition.append(f'(item_in {i[3]} office_bag working_table livingroom)')

        elif i[0]=='prepared_clothes':

            precondition.append(f'(stuff_at {i[1]} {i[2]} {i[3]})')

        
        elif i[0]=='charged':
            precondition.append(f'(stuff_at {i[1]} working_table  livingroom)')


        elif i[0]=='party_at':
            precondition.append('(baked_served cake plate_1 working_table livingroom)')
            precondition.append('(human_switch_on color_lights livingroom)')
            precondition.append('(human_switch_on musicplayer livingroom)')


    precondition = [item for item in precondition if item != '(sliced fruit_salad)']
    precondition = [item for item in precondition if item != '(stuff_at fruit_Salad working_table livingroom)']

    return precondition



def noise_results(od, of, goal, isagentnoisy, ppl, n):
    
    reset_init()

    if isagentnoisy==0:

        random_ppl = random.sample(ppl,k=n)   # n is the number of randomly occuring noises
        multiple_noise_plan(od, of, random_ppl, n)

        """part_1"""

        noisy_action, noise_actual = plan_before_noise(od, of) # Finding the plan before noise 

        if len(noisy_action)==0:
            print("plan is noise free!")

            return (0,0,0)
            
        else:
            
            reset_init()
            directory = 'H4_noise'
            file_name = 'plan_before_noise.txt'
            posn, stuff_posn, preconditions_met = extraction(directory, file_name)
            update_init(posn, stuff_posn) #update the init based on this plan


            """part_1"""  #human_corrects_himself
            goall = putdown_goal(noise_actual)
            append_goal_to_json(goal, goall)
            gen_problem_file('init.txt', goal) 
            run_planner(2)
            # print(goall)
            
            noise_free_cost, total_noise_cost = show_differences(od, of)

            return noisy_action, noise_free_cost, total_noise_cost, preconditions_met
        

    else:

        random_ppl = random.sample(ppl,k=n)
        agent_multiple_noise_plan(od, of, random_ppl, n)

        """part_1"""

        noisy_action, noise_actual = agent_plan_before_noise(od, of) # Finding the plan before noise 

        if len(noisy_action)==0:
            print("plan is noise free!")

            return (0,0,0)

        else:
            
            reset_init()
            directory = 'H4_noise'
            file_name = 'agent_plan_before_noise.txt'
            posn, stuff_posn, preconditions_met = extraction(directory, file_name)
            update_init(posn, stuff_posn) #update the init based on this plan


            """part_1"""  #agent_corrects_himself 
            goall = agent_putdown_goal(noise_actual)
            append_goal_to_json(goal, goall)
            gen_problem_file('init.txt', goal) 
            run_planner(2) # planning for the initial goal
            
            noise_free_cost, total_noise_cost = agent_show_differences(od, of)

            return noisy_action, noise_free_cost, total_noise_cost, preconditions_met

            





def save_plan_after_noise():


    
    def stitch_files(file1, file2, destination):
        with open(destination, 'w') as dest_file:
            for f in [file1, file2]:  
                with open(f, 'r') as source_file:
                    for line in source_file:
                        if not line.startswith(';'):
                            dest_file.write(line)



    nd_2 = 'H4_final'
    nf_2 = f'plan_.txt.{len(os.listdir(nd_2))}'
 

    with open(f'{nd_2}/{nf_2}', 'r') as file:
        original_content = file.read()
    with open(f'{nd_2}/{nf_2}', 'w') as file:
        file.write("\n****\n\n" + original_content)
        
    # Call the function with your file paths
    stitch_files('H4_noise/plan_before_noise.txt', f'{nd_2}/{nf_2}', 'plan_after_noise_ver_4.txt')




def agent_save_plan_after_noise():


    def stitch_files(file1, file2, destination):
        with open(destination, 'w') as dest_file:
            for f in [file1, file2]:  
                with open(f, 'r') as source_file:
                    for line in source_file:
                        if not line.startswith(';'):
                            dest_file.write(line)


    nd_2 = 'H4_final'
    nf_2 = f'plan_.txt.{len(os.listdir(nd_2))}'


 
    with open(f'{nd_2}/{nf_2}', 'r') as file:
        original_content = file.read()
    with open(f'{nd_2}/{nf_2}', 'w') as file:
        file.write("\n****\n" + "\n" + original_content)


    # Call the function with your file paths
    stitch_files('H4_noise/agent_plan_before_noise.txt', f'{nd_2}/{nf_2}', 'agent_plan_after_noise_ver_4.txt')





import random

def run_everything(goal):

    reset_goal(goal)

    gen_problem_file('original_init.txt', goal)
    
    reset_init()

    #running the planner
    run_planner(0)

    #original_results
    od = 'H4_plans'
    of = f'plan_.txt.{len(os.listdir(od))}'


    def isagentN(od, of): #IsAgentNoisy

        with open(f'{od}/{of}', 'r') as file:
            lines = file.readlines()

        li = []

        for l in lines:
            if l.startswith('(human_pick'):
                li.append(l.split())

        recep = ['shelf', 'cabinet', 'rack', 'fridge', 'closet']

        for i in range(len(li) - 1, -1, -1):
            if li[i][2] not in recep:
                    li.pop(i)


        if len(li)==0:
            return 1
        else:
            return 0


    def find_ppl(): # Finding indices of human pick actions

        #original_results
        od = 'H4_plans'
        of = f'plan_.txt.{len(os.listdir(od))}'

        ppl = []
        recep = ['closet', 'rack', 'cabinet', 'shelf', 'fridge']

        with open(f'{od}/{of}', 'r+') as d:

            lines = d.readlines()

        for k, line in enumerate(lines):
            
            if line.startswith('(human_pick') and lines[k].split()[2] in recep:

                ppl.append(k)

        return ppl


    def find_agent_ppl(): # Finding indices of agent pick actions

        #original_results
        od = 'H4_plans'
        of = f'plan_.txt.{len(os.listdir(od))}'

        ppl = []
        recep = ['closet', 'rack', 'cabinet', 'shelf', 'fridge']

        with open(f'{od}/{of}', 'r+') as d:

            lines = d.readlines()

        for k, line in enumerate(lines):
            
            if line.startswith('(agent_pick') and lines[k].split()[2] in recep:

                ppl.append(k)

        return ppl



    ppl = find_ppl()
    a_ppl = find_agent_ppl()
    isagentnoisy = isagentN(od, of)


    n = 1  # Number of noise occurences


    if len(ppl)==0:
        print("Human plan is noise free :)")

    if isagentnoisy==0:

        print("Human action is noisy!")
        # Finding the results
        noisy_action, noise_free_cost, total_noise_cost, preconditions_met = noise_results(od, of, goal, isagentnoisy, ppl, n)

        reset_goal(goal)

        # print(noisy_action)

        save_plan_after_noise()


    if len(a_ppl)==0:
        print("agent plan is noise free :)")

    if isagentnoisy==1:

        print("agent action is noisy!")
        # Finding the results
        noisy_action, noise_free_cost, total_noise_cost, preconditions_met = noise_results(od, of, goal, isagentnoisy, a_ppl, n)

        reset_goal(goal)

        # print(noisy_action)

        agent_save_plan_after_noise()

    
    return preconditions_met, noisy_action, isagentnoisy





def pred_all(goal):
    
    import json
    import re

    with open(goal, 'r') as file:
        f = json.load(file)

    goal_states = [i for i in f.values()]

    pattern = r'\([^\)]+\)'
    goal_states = re.findall(pattern, goal_states[0])
    goal_states = [i.replace('(', '').replace(')', '').split() for i in goal_states]

    precondition = []

    for i in goal_states:

        if i[0]=='cleaned':
            precondition.append(f'(stuff_at {i[1]} sink kitchen)')
            precondition.append(f"(cleaned {i[-1]})")  

        elif i[0]=='sliced':
            precondition.append(f"(sliced {i[-1]})")
            precondition.append(f"(stuff_at {i[-1]} countertop kitchen)")
            
        elif i[0]=='salad_prepared': #changed
            precondition.append(f'(sliced {i[2]})')
            precondition.append(f'(sliced {i[3]})')
            precondition.append(f'(sliced {i[4]})')
            precondition.append(f'(cleaned {i[2]})')
            precondition.append(f'(cleaned {i[3]})')
            precondition.append(f'(cleaned {i[4]})')
            precondition.append(f"(salad_prepared {i[2]} {i[3]} {i[4]})")
            precondition.append('(receptacle_at bowl_1 countertop kitchen)')


        elif i[0]=='cooked':
            precondition.append(f"(cooked {i[-1]})")
            precondition.append(f"(stuff_at {i[-1]} stove_burner_1 kitchen)")

        elif i[0]=='boiled':
            precondition.append(f"(boiled {i[-1]})")
            precondition.append(f"(stuff_at {i[-1]} stove_burner_2 kitchen)")

        elif i[0]=='roasted':
            precondition.append(f"(roasted {i[-1]})")
            precondition.append(f"(stuff_at {i[-1]} stove_burner_3 kitchen)")

        elif i[0]=='egg_prepared':
            precondition.append(f"(egg_prepared {i[-1]})")
            precondition.append(f"(stuff_at {i[-1]} stove_burner_4 kitchen)")

        elif i[0]=='pizza_base_prepared':
            precondition.append("(pizza_base_prepared)")
            precondition.append("(stuff_at prepared_pizza_base countertop kitchen)")

        elif i[0]=='pizza_baked':
            precondition.append("(pizza_baked)")
            precondition.append("(stuff_at baked_pizza oven kitchen)")

        
        elif i[0]=='pizza_served':
            precondition.append(f'(receptacle_at {i[1]} {i[2]} {i[3]})')
            precondition.append(f'(stuff_at baked_pizza {i[2]} {i[3]})')

        elif i[0]=='food_served':

            if i[1]=='boiled_egg':
                precondition.append(f'(receptacle_at metal_pot stove_burner_2 kitchen)')

            elif i[1]=='roasted_chicken':
                precondition.append(f'(receptacle_at pan_1 stove_burner_3 kitchen)')

            elif i[1]=='roasted_sandwich':
                precondition.append(f'(receptacle_at pan_1 stove_burner_3 kitchen)')

            elif i[1]=='omelette':
                precondition.append(f'(receptacle_at pan_2 stove_burner_4 kitchen)')
            else:
                precondition.append(f'(receptacle_at metal_pot stove_burner_1 kitchen)')

                
            precondition.append(f'(receptacle_at {i[2]} {i[3]} {i[4]})')
            precondition.append(f'(stuff_at {i[1]} {i[3]} {i[4]})')

            if i[1]=='roasted_sandwich':
                 precondition.append('(roasted roasted_sandwich)')

            if i[1]=='roasted_chicken':
                 precondition.append('(roasted roasted_chicken)')

            if i[1]=='cooked_cereal':
                 precondition.append('(cooked cooked_cereal)')

            if i[1]=='cooked_pasta':
                 precondition.append('(cooked cooked_pasta)')

            if i[1]=='boiled_egg':
                 precondition.append('(boiled boiled_egg)')


        elif i[0]=='fruit_served':
            
            if i[1]=='fruit_salad':
                precondition.append(f'(receptacle_at {i[2]} {i[3]} {i[4]})')
                precondition.append(f'(stuff_at {i[1]} {i[3]} {i[4]})')


            else:
                precondition.append(f'(sliced {i[1]})')
                precondition.append(f'(receptacle_at {i[2]} {i[3]} {i[4]})')
                precondition.append(f'(stuff_at {i[1]} {i[3]} {i[4]})')
                
                if i[1]=='fruit_salad':
                    precondition.append(f'(cleaned avocado')
                    precondition.append(f'(cleaned apple)')
                    precondition.append(f'(cleaned banana)')

                else:
                    precondition.append(f'(cleaned {i[1]})')



        elif i[0]=='baked':
            precondition.append(f"(baked {i[-1]})")
            precondition.append('(stuff_at mold oven kitchen)')


        elif i[0]=='served_drink':
            precondition.append(f'(receptacle_at {i[2]} {i[3]} {i[4]})')
            precondition.append(f'(stuff_at {i[1]} {i[3]} {i[4]})')
            precondition.append(f"(served_drink {i[1]} {i[2]} {i[3]} {i[4]})")

        elif i[0]=='cleaned_remaining_food':
            precondition.append(f"(cleaned_remaining food {i[-1]})")
            precondition.append(f'(stuff_at {i[1]} dustbin_1 kitchen)')

        elif i[0]=='dishes_cleaned':
            precondition.append("(dishes_cleaned)")

        elif i[0]=='fireextinguished':
            precondition.append(f"(fireextinguished {i[-1]})")

        elif i[0]=='washed_clothes':
            precondition.append("(washed_clothes)")
            precondition.append("(stuff_at cleaned_clothes washingmachine bathroom)")

        elif i[0]=='ironedclothes':
            precondition.append("(ironedclothes)")
            precondition.append("(stuff_at ironedclothes ironing_board livingroom)")

        elif i[0]=='clothes_folded':
            precondition.append("(clothes_folded)")
            precondition.append("(stuff_at folded_clothes ironing_board livingroom)")

        elif i[0]=='laundrydone':
            precondition.append("(washed_clothes)")
            precondition.append("(stuff_at cleaned_clothes washingmachine bathroom)")
            precondition.append("(ironedclothes)")
            precondition.append("(stuff_at ironedclothes ironing_board livingroom)")
            precondition.append("(clothes_folded)")
            precondition.append("(stuff_at folded_clothes ironing_board livingroom)")


        elif i[0]=='room_cleaned':
            precondition.append(f'(b_obj_at vacuum_cleaner {i[1]})')
            precondition.append(f"(room_cleaned {i[-1]})")

        elif i[0]=='office_ready':
            precondition.append('(receptacle_cleaned working_table livingroom)')

        elif i[0]=='bag_prepared':

            precondition.append(f'(item_in {i[1]} office_bag working_table livingroom)')
            precondition.append(f'(item_in {i[2]} office_bag working_table livingroom)')
            precondition.append(f'(item_in {i[3]} office_bag working_table livingroom)')

        elif i[0]=='prepared_clothes':

            precondition.append(f'(prepared_clothes {i[1]} {i[2]} {i[3]})')

        
        elif i[0]=='charged':
            precondition.append(f'(stuff_at {i[1]} working_table  livingroom)')


        elif i[0]=='party_at':
            precondition.append('(baked_served cake plate_1 working_table livingroom)')
            precondition.append('(human_switch_on color_lights livingroom)')
            precondition.append('(human_switch_on musicplayer livingroom)')
            # precondition.append("(party_at livingroom)")
            precondition.append("(baked cake)")
            precondition.append('(receptacle_at plate_1 working_table livingroom)')

        elif i[0]=='provided_at':
            precondition.append(f'(provided_at medicines {i[-2]} {i[-1]})')
            
  


    precondition = [item for item in precondition if item != '(sliced fruit_salad)']
    precondition = [item for item in precondition if item != '(stuff_at fruit_salad working_table livingroom)']

    return precondition






import matplotlib.pyplot as plt

def plot_results(percentage_of_task_covered, t):

    x_labels = list(range(1, n))

    plt.figure(figsize=(10, 6))  

    bars = plt.bar(x_labels, percentage_of_task_covered, color='brown')


    plt.xticks(x_labels)

    # Adding labels for clarity
    plt.xlabel('Goal States')
    plt.ylabel("% Goal comleption")

    # if t == 0:
    #     # plt.title('When noise occured at last pick action')

    # elif t==1:
    #     # plt.title('For randomly occuring noise')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height}%', ha='center', va='bottom')

    plt.show()




def removestuff(preconditions_met):
    for i in range(len(preconditions_met) - 1, -1, -1):
        if preconditions_met[i].split()[0]=='stuff_at' or preconditions_met[i].split()[0]=='human_switch_on' or preconditions_met[i].split()[0]=='agent_switch_on':
            preconditions_met.pop(i)



def no_adaptation_plan(noisy_action, isagentnoisy):

    if isagentnoisy==0:
    
        with open('H4_noise/noisy_plan.txt', 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            line_parts = line.split()
            line_parts = [item.replace('(', '').replace(')', '') for item in line_parts]

            for x in range(len(noisy_action)):

                if noisy_action[x][1]=='metal_pot' and line.startswith('(human_cooks'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='metal_pot' and line.startswith('(agent_cooks'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='metal_pot' and line.startswith('(human_boils'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='metal_pot' and line.startswith('(agent_boils'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='pan_1' and line.startswith('(human_roast'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='pan_1' and line.startswith('(agent_roast'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='pan_2' and line.startswith('(human_prepare_eggs'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='pan_2' and line.startswith('(agent_prepare_eggs'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='banana' and 'sliced_banana' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='apple' and 'sliced_apple' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='avocado' and 'sliced_avocado' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='cereal' and 'cooked_cereal' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='pasta' and 'cooked_pasta' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='raw_egg' and 'boiled_egg' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='egg' and 'omelette' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='bread' and 'roasted_sandwich' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'    

                if noisy_action[x][1]=='chicken' and 'roasted_chicken' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='bowl_1' and 'fruit_salad' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='banana' and 'fruit_salad' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='apple' and 'fruit_salad' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='avocado' and 'fruit_salad' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if line_parts[1]==noisy_action[x][1]:
                    lines[i] = 'NOT_APPLICABLE\n'

                if len(line_parts)>2:
                    if line_parts[2] == noisy_action[x][1]:
                        lines[i] = 'NOT_APPLICABLE\n'

        with open('no_adaptation/no_adaptation_plan.txt', 'w') as file:
            file.writelines(lines)


    elif isagentnoisy==1:
    
        with open('H4_noise/agent_noisy_plan.txt', 'r') as file:
            lines = file.readlines()


        for i, line in enumerate(lines):
            line_parts = line.split()
            line_parts = [item.replace('(', '').replace(')', '') for item in line_parts]

            for x in range(len(noisy_action)):

                if noisy_action[x][1]=='metal_pot' and line.startswith('(human_cooks'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='metal_pot' and line.startswith('(agent_cooks'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='metal_pot' and line.startswith('(human_boils'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='metal_pot' and line.startswith('(agent_boils'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='pan_1' and line.startswith('(human_roast'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='pan_1' and line.startswith('(agent_roast'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='pan_2' and line.startswith('(human_prepare_eggs'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='pan_2' and line.startswith('(agent_prepare_eggs'):
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='banana' and 'sliced_banana' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='apple' and 'sliced_apple' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='avocado' and 'sliced_avocado' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='cereal' and 'cooked_cereal' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='pasta' and 'cooked_pasta' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='raw_egg' and 'boiled_egg' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='egg' and 'omelette' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='bread' and 'roasted_sandwich' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'    

                if noisy_action[x][1]=='chicken' and 'roasted_chicken' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='bowl_1' and 'fruit_salad' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='banana' and 'fruit_salad' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='apple' and 'fruit_salad' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if noisy_action[x][1]=='avocado' and 'fruit_salad' in line_parts:
                    lines[i] = 'NOT_APPLICABLE\n'

                if line_parts[1]==noisy_action[x][1]:
                    lines[i] = 'NOT_APPLICABLE\n'

                if len(line_parts)>2:
                    if line_parts[2] == noisy_action[x][1]:
                        lines[i] = 'NOT_APPLICABLE\n'

        with open('no_adaptation/no_adaptation_plan.txt', 'w') as file:
            file.writelines(lines)




import os

def remove_last_line(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    with open(file_name, 'w') as dest:

        for l in lines:
            if l.startswith(';'):
                continue
            dest.write(l)



def clean_text_file(file_path):
    
    with open(file_path, 'r') as file, open(file_path + "_cleaned", 'w') as output_file:

        for line in file:
            stripped_line = line.strip()
            clean_line = stripped_line.replace('*', '')
            if clean_line:
                output_file.write(clean_line + '\n')



def show_42_cost():

    directory = 'H4_noise'
    file_name = 'noisy_plan.txt'

    with open(f'{directory}/{file_name}', 'r') as file:
            lines = file.readlines()

    noise_cost = int(lines[-1].split()[3])


    nd_2 = 'H4_42'
    nf_2 = f'plan_.txt.{len(os.listdir(nd_2))}'

    with open(f'{nd_2}/{nf_2}', 'r') as file:
            lines = file.readlines()

    recovery_cost = int(lines[-1].split()[3])


    return noise_cost+recovery_cost



def STITCH_1(isagentnoisy):


    
    def stitch_files(file1, file2, destination):
        with open(destination, 'w') as dest_file:
            for f in [file1, file2]:  
                with open(f, 'r') as source_file:
                    for line in source_file:
                        if not line.startswith(';'):
                            dest_file.write(line)

    
    if isagentnoisy == 0:
        nd_1 = 'H4_noise'
        nf_1 = 'noisy_plan.txt'

        nd_2 = 'H4_42'
        nf_2 = f'plan_.txt.{len(os.listdir(nd_2))}'
            
        # Call the function with your file paths
        stitch_files(f'{nd_1}/{nf_1}', f'{nd_2}/{nf_2}', '42_plan.txt')
    
    else:

        nd_1 = 'H4_noise'
        nf_1 = 'agent_noisy_plan.txt'

        nd_2 = 'H4_42'
        nf_2 = f'plan_.txt.{len(os.listdir(nd_2))}'
            
        # Call the function with your file paths
        stitch_files(f'{nd_1}/{nf_1}', f'{nd_2}/{nf_2}', '42_plan.txt')


def STITCH_2():


    
    def stitch_files(file1, file2, destination):
        with open(destination, 'w') as dest_file:
            for f in [file1, file2]:  
                with open(f, 'r') as source_file:
                    for line in source_file:
                        if not line.startswith(';'):
                            dest_file.write(line)


    nd_1 = 'no_adaptation'
    nf_1 = 'no_adaptation_plan.txt'

    nd_2 = 'H4_42'
    nf_2 = f'plan_.txt.{len(os.listdir(nd_2))}'
        
    # Call the function with your file paths
    stitch_files(f'{nd_1}/{nf_1}', f'{nd_2}/{nf_2}', '42_plan_updated.txt')




def clean_text_file(file_path):
    
    with open(file_path, 'r') as file, open(file_path + "_cleaned", 'w') as output_file:

        for line in file:
            stripped_line = line.strip()
            clean_line = stripped_line.replace('*', '')
            if clean_line:
                output_file.write(clean_line + '\n')



def remove_NOT_APPLICABLE():
    with open('42_sliced/42_plan_updated_sliced.txt', 'r') as file:
        lines = file.readlines()

    with open('42_sliced/42_plan_updated_sliced.txt', 'w') as new_file:
        for line in lines:
            if line.strip() != 'NOT_APPLICABLE':
                new_file.write(line)




import re

def find_per(goal, preconditions_met_actual):

    with open(goal, 'r') as file:
        f = json.load(file)

    goal_states = [i for i in f.values()]

    pattern = r'\([^\)]+\)'
    goal_states = re.findall(pattern, goal_states[0])
    goal_states = [i.replace('(', '').replace(')', '').split() for i in goal_states]

    precondition = []

    satisfied = []

    for i in goal_states:

        if i[0]=='cleaned':
            precondition.append(f'(stuff_at {i[1]} sink kitchen)')
            precondition.append(f"(cleaned {i[-1]})")  

        elif i[0]=='sliced':
            precondition.append(f"(sliced {i[-1]})")
            precondition.append(f"(stuff_at {i[-1]} countertop kitchen)")
            
        elif i[0]=='salad_prepared': #changed
            precondition.append(f'(sliced {i[2]})')
            precondition.append(f'(sliced {i[3]})')
            precondition.append(f'(sliced {i[4]})')
            precondition.append(f'(cleaned {i[2]})')
            precondition.append(f'(cleaned {i[3]})')
            precondition.append(f'(cleaned {i[4]})')
            precondition.append(f"(salad_prepared {i[2]} {i[3]} {i[4]})")
            precondition.append('(receptacle_at bowl_1 countertop kitchen)')


        elif i[0]=='cooked':
            precondition.append(f"(cooked {i[-1]})")
            precondition.append(f"(stuff_at {i[-1]} stove_burner_1 kitchen)")

        elif i[0]=='boiled':
            precondition.append(f"(boiled {i[-1]})")
            precondition.append(f"(stuff_at {i[-1]} stove_burner_2 kitchen)")

        elif i[0]=='roasted':
            precondition.append(f"(roasted {i[-1]})")
            precondition.append(f"(stuff_at {i[-1]} stove_burner_3 kitchen)")

        elif i[0]=='egg_prepared':
            precondition.append(f"(egg_prepared {i[-1]})")
            precondition.append(f"(stuff_at {i[-1]} stove_burner_4 kitchen)")

        elif i[0]=='pizza_base_prepared':
            precondition.append("(pizza_base_prepared)")
            precondition.append("(stuff_at prepared_pizza_base countertop kitchen)")

        elif i[0]=='pizza_baked':
            precondition.append("(pizza_baked)")
            precondition.append("(stuff_at baked_pizza oven kitchen)")

        
        elif i[0]=='pizza_served':
            precondition.append(f'(receptacle_at {i[1]} {i[2]} {i[3]})')
            precondition.append(f'(stuff_at baked_pizza {i[2]} {i[3]})')

        elif i[0]=='food_served':

            precondition.append(f'(food_served {i[1]} {i[2]} {i[3]} {i[4]})')

            if i[1]=='boiled_egg':
                precondition.append(f'(receptacle_at metal_pot stove_burner_2 kitchen)')

            elif i[1]=='roasted_chicken':
                precondition.append(f'(receptacle_at pan_1 stove_burner_3 kitchen)')

            elif i[1]=='roasted_sandwich':
                precondition.append(f'(receptacle_at pan_1 stove_burner_3 kitchen)')

            elif i[1]=='omelette':
                precondition.append(f'(receptacle_at pan_2 stove_burner_4 kitchen)')
            else:
                precondition.append(f'(receptacle_at metal_pot stove_burner_1 kitchen)')

                
            precondition.append(f'(receptacle_at {i[2]} {i[3]} {i[4]})')
            precondition.append(f'(stuff_at {i[1]} {i[3]} {i[4]})')

            if i[1]=='roasted_sandwich':
                    precondition.append('(roasted roasted_sandwich)')

            if i[1]=='roasted_chicken':
                    precondition.append('(roasted roasted_chicken)')

            if i[1]=='cooked_cereal':
                    precondition.append('(cooked cooked_cereal)')

            if i[1]=='cooked_pasta':
                    precondition.append('(cooked cooked_pasta)')

            if i[1]=='boiled_egg':
                    precondition.append('(boiled boiled_egg)')


        elif i[0]=='fruit_served':
            
            if i[1]=='fruit_salad':
                precondition.append(f'(receptacle_at {i[2]} {i[3]} {i[4]})')
                precondition.append(f'(stuff_at {i[1]} {i[3]} {i[4]})')


            else:
                precondition.append(f'(sliced {i[1]})')
                precondition.append(f'(receptacle_at {i[2]} {i[3]} {i[4]})')
                precondition.append(f'(stuff_at {i[1]} {i[3]} {i[4]})')
                
                if i[1]=='fruit_salad':
                    precondition.append(f'(cleaned avocado')
                    precondition.append(f'(cleaned apple)')
                    precondition.append(f'(cleaned banana)')

                else:
                    precondition.append(f'(cleaned {i[1]})')



        elif i[0]=='baked':
            precondition.append(f"(baked {i[-1]})")
            precondition.append('(stuff_at mold oven kitchen)')


        elif i[0]=='served_drink':
            precondition.append(f'(receptacle_at {i[2]} {i[3]} {i[4]})')
            precondition.append(f'(stuff_at {i[1]} {i[3]} {i[4]})')
            precondition.append(f"(served_drink {i[1]} {i[2]} {i[3]} {i[4]})")

        elif i[0]=='cleaned_remaining_food':
            precondition.append(f"(cleaned_remaining food {i[-1]})")
            precondition.append(f'(stuff_at {i[1]} dustbin_1 kitchen)')

        elif i[0]=='dishes_cleaned':
            precondition.append("(dishes_cleaned)")

        elif i[0]=='fireextinguished':
            precondition.append(f"(fireextinguished {i[-1]})")

        elif i[0]=='washed_clothes':
            precondition.append("(washed_clothes)")
            precondition.append("(stuff_at cleaned_clothes washingmachine bathroom)")

        elif i[0]=='ironedclothes':
            precondition.append("(ironedclothes)")
            precondition.append("(stuff_at ironedclothes ironing_board livingroom)")

        elif i[0]=='clothes_folded':
            precondition.append("(clothes_folded)")
            precondition.append("(stuff_at folded_clothes ironing_board livingroom)")

        elif i[0]=='laundrydone':
            precondition.append("(washed_clothes)")
            precondition.append("(stuff_at cleaned_clothes washingmachine bathroom)")
            precondition.append("(ironedclothes)")
            precondition.append("(stuff_at ironedclothes ironing_board livingroom)")
            precondition.append("(clothes_folded)")
            precondition.append("(stuff_at folded_clothes ironing_board livingroom)")


        elif i[0]=='room_cleaned':
            precondition.append(f'(b_obj_at vacuum_cleaner {i[1]})')
            precondition.append(f"(room_cleaned {i[-1]})")

        elif i[0]=='office_ready':
            precondition.append('(receptacle_cleaned working_table livingroom)')

        elif i[0]=='bag_prepared':

            precondition.append(f'(item_in {i[1]} office_bag working_table livingroom)')
            precondition.append(f'(item_in {i[2]} office_bag working_table livingroom)')
            precondition.append(f'(item_in {i[3]} office_bag working_table livingroom)')

        elif i[0]=='prepared_clothes':

            precondition.append(f'(prepared_clothes {i[1]} {i[2]} {i[3]})')

        
        elif i[0]=='charged':
            precondition.append(f'(stuff_at {i[1]} working_table  livingroom)')


        elif i[0]=='party_at':
            precondition.append('(baked_served cake plate_1 working_table livingroom)')
            precondition.append('(human_switch_on color_lights livingroom)')
            precondition.append('(human_switch_on musicplayer livingroom)')
            precondition.append("(baked cake)")
            precondition.append('(receptacle_at plate_1 working_table livingroom)')

        elif i[0]=='provided_at':
            precondition.append(f'(provided_at medicines {i[-2]} {i[-1]})')


        precondition = [item for item in precondition if item != '(sliced fruit_salad)']
        precondition = [item for item in precondition if item != '(stuff_at fruit_salad working_table livingroom)']

        precondition = [element.replace('(', '').replace(')', '') for element in precondition]
        removestuff(precondition)

        pp = 0
        ll = len(precondition)

        for p in precondition:
            if p in preconditions_met_actual:
                pp+=1
        
        if pp==ll:
            satisfied.append(1)

        precondition = []


    return sum(satisfied)/len(goal_states)

        

import random
import re


def final_run(goals, isagentnoisy):

    results = []

    x = 1

    for goal in goals:

        g = []

        reset_goal(goal)
        gen_problem_file('original_init.txt', goal)
        reset_init()

        #running the planner
        run_planner(0)

        #original_results
        od = 'H4_plans'
        of = f'plan_.txt.{len(os.listdir(od))}'


        def isagentN(od, of): #IsAgentNoisy

            with open(f'{od}/{of}', 'r') as file:
                lines = file.readlines()

            li = []

            for l in lines:
                if l.startswith('(human_pick'): #counts the numbers of human pick actions.
                    li.append(l.split())

            recep = ['shelf', 'cabinet', 'rack', 'fridge', 'closet']

            for i in range(len(li) - 1, -1, -1):
                if li[i][2] not in recep:
                        li.pop(i)


            if len(li)==0:
                return 1
            else:
                return 0


        def find_ppl(): 

            #original_results
            od = 'H4_plans'
            of = f'plan_.txt.{len(os.listdir(od))}'

            ppl = []
            recep = ['closet', 'rack', 'cabinet', 'shelf', 'fridge']

            with open(f'{od}/{of}', 'r+') as d:

                lines = d.readlines()

            for k, line in enumerate(lines):
                
                if line.startswith('(human_pick') and lines[k].split()[2] in recep:

                    ppl.append(k)

            return ppl


        def find_agent_ppl(): 

            #original_results
            od = 'H4_plans'
            of = f'plan_.txt.{len(os.listdir(od))}'

            ppl = []
            recep = ['closet', 'rack', 'cabinet', 'shelf', 'fridge']

            with open(f'{od}/{of}', 'r+') as d:

                lines = d.readlines()

            for k, line in enumerate(lines):
                
                if line.startswith('(agent_pick') and lines[k].split()[2] in recep:

                    ppl.append(k)

            return ppl



        ppl = find_ppl()
        a_ppl = find_agent_ppl()
        # isagentnoisy = isagentN(od, of)


        if len(ppl)==0:
            print("Human plan is noise free :)")

        if len(a_ppl)==0:
            print("agent plan is noise free :)")

        if isagentnoisy==0:
                
            for i in range(len(ppl)):

                od = 'H4_plans'
                of = f'plan_.txt.{len(os.listdir(od))}'

                print("Human action is noisy!")
                noisy_action, noise_free_cost, total_noise_cost, preconditions_met = noise_results(od, of, goal, isagentnoisy, ppl, i+1)

                reset_goal(goal)

                save_plan_after_noise()

                no_adaptation_plan(noisy_action, isagentnoisy)

        
                # Slicing the no adaptation plan

                od = 'no_adaptation'
                of = 'no_adaptation_plan.txt'
                posn, stuff_posn, preconditions_met_actual = extraction(od, of)
                update_init(posn, stuff_posn) 
                gen_problem_file('init.txt', goal) 
                run_planner(5)

                contents = os.listdir('H4_42')

                if len(contents)==0:
                    print(f"{x}_{i}: H4_42 folder is empty!")
                    continue

                STITCH_1(isagentnoisy)
                remove_last_line('42_plan.txt')
                clean_text_file('plan_after_noise_ver_4.txt')




                with open('plan_after_noise_ver_4.txt_cleaned', 'r') as file:
                    lines = file.readlines()

                len_adaptation = len(lines)

                with open('42_plan.txt', 'r') as file:
                    lines = file.readlines()

                len_no_adaptation = len(lines)


                

                diff = len_no_adaptation - len_adaptation

                
            
                STITCH_2()
                
                with open('42_plan_updated.txt', 'r') as file:
                    lines = file.readlines()

                len_updated = len(lines)

                with open('42_sliced/42_plan_updated_sliced.txt', 'w') as file:
                    for i in range(len_updated-abs(diff)):
                        file.write(lines[i])

                
                # Preconditions met
                oda = '42_sliced'
                ofa = '42_plan_updated_sliced.txt'

                remove_NOT_APPLICABLE()

                
                posn, stuff_posn, preconditions_met_actual = extraction(oda, ofa)
                removestuff(preconditions_met_actual)

                for i in range(len(preconditions_met) - 1, -1, -1):
                    if preconditions_met[i]=='receptacle_at plate_1 countertop kitchen' or preconditions_met[i]=='receptacle_at plate_2 countertop kitchen':
                        preconditions_met.pop(i)

                for i in range(len(preconditions_met_actual) - 1, -1, -1):
                    if preconditions_met_actual[i]=='receptacle_at plate_1 countertop kitchen' or preconditions_met_actual[i]=='receptacle_at plate_2 countertop kitchen':
                        preconditions_met_actual.pop(i)
                        

                # Finding percentage
                percent = find_per(goal, preconditions_met_actual)
                g.append(percent)






        if isagentnoisy==1:
                
            for i in range(len(a_ppl)):

                od = 'H4_plans'
                of = f'plan_.txt.{len(os.listdir(od))}'

                print("agent action is noisy!")
                noisy_action, noise_free_cost, total_noise_cost, preconditions_met = noise_results(od, of, goal, isagentnoisy, a_ppl, i+1)

                reset_goal(goal)

                agent_save_plan_after_noise()

                no_adaptation_plan(noisy_action, isagentnoisy)

        
                # Slicing the no adaptation plan

                od = 'no_adaptation'
                of = 'no_adaptation_plan.txt'
                posn, stuff_posn, preconditions_met_actual = extraction(od, of)
                update_init(posn, stuff_posn) 
                gen_problem_file('init.txt', goal) 
                run_planner(5)

                contents = os.listdir('H4_42')

                if len(contents)==0:
                    print(f"{x}_{i}: H4_42 folder is empty!")
                    continue

                STITCH_1(isagentnoisy)
                remove_last_line('42_plan.txt')
                clean_text_file('agent_plan_after_noise_ver_4.txt')




                with open('agent_plan_after_noise_ver_4.txt_cleaned', 'r') as file:
                    lines = file.readlines()

                len_adaptation = len(lines)

                with open('42_plan.txt', 'r') as file:
                    lines = file.readlines()

                len_no_adaptation = len(lines)


                

                diff = len_no_adaptation - len_adaptation

                
            
                STITCH_2()
                with open('42_plan_updated.txt', 'r') as file:
                    lines = file.readlines()

                len_updated = len(lines)

                with open('42_sliced/42_plan_updated_sliced.txt', 'w') as file:
                    for i in range(len_updated-abs(diff)):
                        file.write(lines[i])

                
                # Preconditions met
                oda = '42_sliced'
                ofa = '42_plan_updated_sliced.txt'

                remove_NOT_APPLICABLE()

                
                posn, stuff_posn, preconditions_met_actual = extraction(oda, ofa)
                removestuff(preconditions_met_actual)

                for i in range(len(preconditions_met) - 1, -1, -1):
                    if preconditions_met[i]=='receptacle_at plate_1 countertop kitchen' or preconditions_met[i]=='receptacle_at plate_2 countertop kitchen':
                        preconditions_met.pop(i)

                for i in range(len(preconditions_met_actual) - 1, -1, -1):
                    if preconditions_met_actual[i]=='receptacle_at plate_1 countertop kitchen' or preconditions_met_actual[i]=='receptacle_at plate_2 countertop kitchen':
                        preconditions_met_actual.pop(i)
                        

                # Finding percentage
                percent = find_per(goal, preconditions_met_actual)
                g.append(percent)


        
        results.append(g)
        x+=1

        return results
        




# goals = ['goals/H4_goal_1.json', 'goals/H4_goal_2.json', 'goals/H4_goal_3.json', 'goals/H4_goal_4.json', 'goals/H4_goal_5.json', 'goals/H4_goal_6.json', 'goals/H4_goal_7.json', 'goals/H4_goal_8.json', 'goals/H4_goal_9.json', 'goals/H4_goal_10.json', 'goals/H4_goal_11.json', 'goals/H4_goal_12.json', 'goals/H4_goal_13.json', 'goals/H4_goal_14.json', 'goals/H4_goal_15.json', 'goals/H4_goal_16.json', 'goals/H4_goal_17.json', 'goals/H4_goal_18.json']


goals = ['goals/H4_goal_16.json']


"""

isagentnoise=0  ; Human is noisy
isagentnoise=1  ; Agent is noisy

"""

results = final_run(goals, isagentnoisy=0)
print(results)





