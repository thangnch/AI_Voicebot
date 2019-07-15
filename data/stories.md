<!------- Field 01. Trò chuyện ----------------------------------------->

## Gặp tổng đài -có chào
* greet
  - utter_greet
* give_name 
  - action_save_cust_info
  - utter_greet_with_name
* meet_human
  - utter_meet_human
  
## Gặp tổng đài -ko chào
* meet_human
  - utter_meet_human

## Chào hỏi
* greet
  - utter_greet
* give_name 
  - action_save_cust_info
  - utter_greet_with_name
* inform_yes
  - utter_greet_with_name

## Thanks - có chào
* greet
  - utter_greet
* give_name 
  - action_save_cust_info
  - utter_greet_with_name
* thank
  - utter_thank
  - utter_greet_with_name

## Thanks - Không chào
* thank
  - utter_thank
  - utter_greet_with_name
  
## Chửi - Không chào
* shit
  - utter_shit
  - utter_greet_with_name

## Chatchit - Có chào
* greet
  - utter_greet
* give_name 
  - action_save_cust_info
  - utter_greet_with_name
* chatchit
  - utter_chatchit
  - utter_greet_with_name

## Chatchit - Ko chào
* chatchit
  - utter_chatchit
  - utter_greet_with_name
  
## Chửi - Có chào
* greet
  - utter_greet
* give_name 
  - action_save_cust_info
  - utter_greet_with_name
* shit
  - utter_shit
  - utter_greet_with_name


  
## Bye
* greet
  - utter_greet
* give_name 
  - action_save_cust_info
  - utter_greet_with_name
* bye
  - utter_bye
  
## té
* inform_no
  - utter_bye