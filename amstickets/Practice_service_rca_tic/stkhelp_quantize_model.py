import fasttext

model = fasttext.load_model("model_stkhelp.bin")

model.quantize(input=None,
                  qout=False,
                  cutoff=0,
                  retrain=False,
                  epoch=None,
                  lr=None,
                  thread=None,
                  verbose=None,
                  dsub=2,
                  qnorm=False,
                 )

# Save Quantized model
model.save_model('model_stkhelp_q.bin')