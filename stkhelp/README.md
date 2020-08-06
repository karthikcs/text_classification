# Text classfication Softtek Help tickets

## Objective 
Huge number of tickets are getting created in Softtek help portal. We also have a intelligent chatbot to help people of Softtek. We need an intelligent text classifier based on ML, which automatically classifies the ticket based on the text 

## Technical details 
This text classification solution was done using ``fasttext`` library using python 

## Training Data 
Files

- ``stkhelp.csv`` - Labelled file with 57888 records of 2020: Initially only one class (label) was given. We had more than 250 classes. That is a huge set for classification problem. Later we also added high level (Department) information as another label. 

  - Label 1 - Department Information 
  - Label 2 - Actual class of the ticket 
  - Description - Actual text to be considered 

  The text in this file is not cleaned

- ``stkhelp_ft`` - New file created after Simple leaning is done. Input is ``stkhelp.csv``

  - converted everything to lower case 
  - removed urls 
  - removed text in square brackets 
  - removed punctuation texts

  Program ```conver2ft.py``` is used to clean the file and convert to the format required by ```fasttext```
  Every line have the format as given below 

  ```
  label1 label2 text
  ```

- ``stkhelp.train`` and ``stkhelp.test``` - 

  The converted file ``stkhelp_ft`` has been shuffled (randomised) into new file ``stkhelp_final``. Then top 80% of the lines (~47000) lines are written into train file and 20% of the bottom file is written into test file. Following commands are executed to produce these files

  ```
  shuf stkhelp_ft > stkhelp_final
  head -n 47000 stkhelp_final > stkhelp.train
  tail -n 10888 stkhelp_final > stkhelp.test
  ```

- Training Execution: Execute stkhelp.py to train and save the model into file ``model_stkhelp.bin``

Quantized the model using ```quantize_model.py```. The quantized model is stored in ```model_stkhelp_q1.bin```.

For this model following was the output

  ```
karthikcs105@machine-learning2-n1-2vcpu-75:~/text_classification/stkhelp$ python3 stkhelp.py -t
Progress: 100.0% Trials:   16 Best score:  0.584377 ETA:   0h 0m 0s
Training again with best arguments
Read 1M words
Number of words:  56437
Number of labels: 238
Progress: 100.0% words/sec/thread:  442209 lr:  0.000000 avg.loss:  2.303474 ETA:   0h 0m 0s

  ```

It has F1 Score of around **58.43%**

  ```
karthikcs105@machine-learning2-n1-2vcpu-75:~/text_classification/stkhelp$ python3 stkhelp.py -v stkhelp.test
Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.
(10888, 0.8763776634827333, 0.4383297349441867)
  ```
  Precision = 87.64%   - Out of predicted labels how many were correct

  Recall = 43.83%  - Out of correct (actual) labels how many were predicted 


- Testing the model

```
python3 stkhelp.py -p "RAM memory purchase Purchase and install additional 8GB RAM memory to Vincent Chen's laptop "

(('__label__it_request', '__label__install_remove_hardware', '__label__install_uninstall_software'), array([0.50893319, 0.1840259 , 0.10763644]))

python3 stkhelp.py -p "Please install additional 8GB RAM on Sunesh's laptop"

(('__label__it_request', '__label__install_uninstall_software', '__label__install_remove_hardware'), array([0.58480269, 0.27601266, 0.06017245]))

python3 stkhelp.py -p "Me podrian ayudar a saber si esta persona puede re ingresar a Softtek? estuvo en GE "

(('__label__digital_office', '__label__hra', '__label__application_access'), array([0.28647593, 0.09006527, 0.08896956]))

python3 stkhelp.py -p "Ander Li's offboard process"

(('__label__it_request', '__label__assign_unassign_equipment', '__label__install_uninstall_software'), array([0.497612  , 0.15583676, 0.03963695]))

python3 stkhelp.py -p "Favor de ayudarnos a crear un curso de BCP/DRP en Ingles en SU. Muchas gracias"

(('__label__talent_dev', '__label__skillsoft_license_request', '__label__application_access'), array([0.32552585, 0.22685926, 0.06600231]))

python3 stkhelp.py -p "Can you please assign Finance course to Sunesh" 

(('__label__it_request', '__label__talent_dev', '__label__business_english_level_assessment'), array([0.22885799, 0.21769826, 0.08369628]))

python3 stkhelp.py -p "Please provide license for agile exm"

(('__label__talent_dev', '__label__skillsoft_license_request', '__label__it_request'), array([0.39193755, 0.20615728, 0.13279888]))

python3 stkhelp.py -p "Proporcione una licencia para un examen agile"

(('__label__talent_dev', '__label__skillsoft_license_request', '__label__accessories_purchase'), array([0.47163901, 0.412476  , 0.0895598 ]))

python3 stkhelp.py -p "revocar el acceso de CDS a Shasank"

(('__label__facilities', '__label__access_request', '__label__cancel_access'), array([0.52787006, 0.2197216 , 0.18792981]))

python3 stkhelp.py -p "Favor revocar el acceso de CDS a Shasank"

(('__label__facilities', '__label__access_request', '__label__cancel_access'), array([0.53092462, 0.21247984, 0.17717309]))

python3 stkhelp.py -p "Recientemente he tenido que  pedir a compañeros de trabajo que  me ayuden a tomar la figura de aval  para la renta de  una casa en Aguascalientes."

(('__label__it_request', '__label__hra', '__label__install_uninstall_software'), array([0.16559854, 0.08233529, 0.0560865 ]))

python3 stkhelp.py -p "Favor enviar las liquidaciones del mes de Noviembre y Enero a mi email gracias"

(('__label__hra', '__label__rhotras_solicitudes', '__label__programacion_de_reembolso'), array([0.27939779, 0.06685966, 0.03052883]))

python3 stkhelp.py -p "favor de enviar las liquidaciones del mes de Agosto y Septiembre a mi casilla de correo muchas gracias"

(('__label__facilities', '__label__hra', '__label__delivery'), array([0.1265507 , 0.11821415, 0.10158942]))

python3 stkhelp.py -p "Necesito por favor cambiar a las siguientes personas del calendarion Mexicano al Americano"

(('__label__hra', '__label__digital_office', '__label__rhotras_solicitudes'), array([0.25856879, 0.2027135 , 0.11258645]))
```

We can take model and use it in any other requirements. May we can integrate to a chat bot or any other API.. 

GOOD LUCK

---


## Update 27-Jul-2020. Removed Stop words 
### Removed both English and Spanish Stopwords 

Following was the results

```
python3 stkhelp.py -t
Progress: 100.0% Trials:   23 Best score:  0.588736 ETA:   0h 0m 0s
Training again with best arguments
Read 1M words
Number of words:  55317
Number of labels: 235
Progress: 100.0% words/sec/thread:  131741 lr:  0.000000 avg.loss:  1.987040 ETA:   0h 0m 0s
```
Overall F1 Score - **58.87%** Slightly improved from 58.43% in the first version

Following was Precision and Recall

```
(10888, 0.8926340925789861, 0.4465426142889961)
```

Precision = 89.26%   - Out of predicted labels how many were correct

Recall = 44.65%  - Out of correct (actual) labels how many were predicted 

These scores have also improved slightly.
Model quantized and  stored in ```model_stkhelp_q2.bin```

----
Date: 3-Aug-2020
Made modification  to remove all numbers and words before training. Following is the results after 1 hr traning 

```
karthikcs105@machine-learning2-n1-2vcpu-75:~/text_classification/stkhelp$ python3 stkhelp.py -t
Warning : wordNgrams is manually set to a specific value. It will not be automatically optimized.
Progress: 100.0% Trials:   22 Best score:  0.587482 ETA:   0h 0m 0s
Training again with best arguments
Read 1M words
Number of words:  40673
Number of labels: 238
Progress: 100.0% words/sec/thread:  171158 lr:  0.000000 avg.loss:  1.972504 ETA:   0h 0m 0s
```