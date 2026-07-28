"""Hinglish teaching prose — parallel to teach.BANK.

Keyed by each BANK entry's FIRST key, so this file stays correct even if the
English bank is reordered. Code samples are reused from BANK (code is code);
only the prose is Hinglish. Missing keys fall back to the English prose, so
partial coverage degrades gracefully instead of breaking.
"""
from __future__ import annotations

from teach import BANK, teach

HI: dict[str, dict[str, str]] = {
    "virtual environment": {
        "plain": "Virtual environment ek project ke liye Python ki private copy hai. Iske bina do projects ek hi library version ke liye ladte hain. Ek baar banao, activate karo, usi me install karo, aur exact versions freeze kar do taaki koi aur aapka result dobara bana sake.",
        "remember": "Agar `pip install` chala par import fail ho raha hai, to aapne kisi doosre interpreter me install kiya hai.",
        "mistake": "Globally install karna, phir sochna ki colleague ki machine par alag result kyun aa raha hai.",
    },
    "jupyter": {
        "plain": "Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.",
        "remember": "'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.",
        "mistake": "Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.",
    },
    "list comprehension": {
        "plain": "Comprehension poori list turant bana deti hai; generator ek-ek item deta hai aur puri sequence memory me kabhi nahi rakhta. RAM se badi dataset par generator hi 'chalta hai' aur 'crash' ke beech ka farq hai.",
        "remember": "Generator sirf ek baar consume hota hai — doosre pass ke liye use dobara banao.",
        "mistake": "Generator par `len()` lagana, ya do baar iterate karke doosri baar khaali paana.",
    },
    "numpy array": {
        "plain": "NumPy numbers ko ek continuous typed block me rakhta hai aur loops C me chalata hai. Vectorised code (poore array par operation) aksar Python loop se 50-100x tez hota hai aur maths jaisa padhta hai. Broadcasting chhoti shapes ko bina copy kiye stretch kar deta hai.",
        "remember": "`axis=0` rows ko collapse karta hai (columns ke neeche); `axis=1` columns ko (ek row ke aar-paar).",
        "mistake": "Python loop me array elements ghumana, vectorised operation use karne ke bajaye.",
    },
    "pandas": {
        "plain": "DataFrame ek table hai jisme labelled columns aur ek index hota hai. Asli ML ka 80% kaam tables ko reshape karna hi hai: load, clean, group, join, aggregate. `groupby` aur `merge` acche se seekh lo to zyadatar data sawaal bina loop likhe hal ho jaate hain.",
        "remember": "Merge se pehle aur baad me `df.shape` zaroor check karo — chupke se rows badhna matlab duplicate keys.",
        "mistake": "Chained assignment (`df[df.a > 1]['b'] = 0`) jo copy par likhta hai aur kuch nahi badalta.",
    },
    "missing value": {
        "plain": "Missing data information hai, sirf noise nahi. Kuch bharne se pehle poochho ki **kyun** missing hai: jo sensor sirf load par fail hota hai wo randomly missing nahi hai. Phir chuno: rows drop, column drop, statistic se fill, ya ek explicit 'ye missing tha' indicator column.",
        "remember": "Fill karne wali statistic sirf TRAIN split par nikalo, phir test par lagao.",
        "mistake": "Poore dataset ke mean se fill karna — ye test ki information training me leak kar deta hai.",
    },
    "matplotlib": {
        "plain": "Model se pehle plot karo. Histogram skew aur outliers dikhata hai, scatter non-linearity, aur residuals ka plot batata hai ki model systematically galat kahan hai. Paanch minute ka plotting ghanton ki confused tuning bacha deta hai.",
        "remember": "Axes par label lagao. Bina label ka plot sajावat hai, evidence nahi.",
        "mistake": "Sirf accuracy number dekh kar model judge karna, data ko kabhi dekhe bina.",
    },
    "vector": {
        "plain": "Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.",
        "remember": "Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.",
        "mistake": "Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.",
    },
    "matrix multiplication": {
        "plain": "Matrix ek linear transformation hai. Matrices ko multiply karna transformations ko jodta hai — neural network ki layers stack karna bilkul yahi hai. Shapes milni chahiye: (m,k) @ (k,n) -> (m,n); andar wale dimensions match hone chahiye aur wahi gayab ho jaate hain.",
        "remember": "Har shape error ko 'andar wale dimensions match nahi hue' padho aur shapes print kar do.",
        "mistake": "`Ax=b` solve karne ke liye `np.linalg.inv` uthana, jabki `np.linalg.solve` zyada safe hai.",
    },
    "eigen": {
        "plain": "Eigenvectors wo directions hain jinhe matrix sirf khinchta hai, ghumata nahi; eigenvalue khinchne ka factor hai. SVD isi ko har matrix ke liye general kar deta hai aur PCA, low-rank compression aur LoRA adapters ke peeche yahi engine hai.",
        "remember": "Descending order me sorted singular values batate hain ki kitne dimensions me sach me information hai.",
        "mistake": "Bina scaling ke PCA/SVD chalana, jisse sabse badi unit wala column har component par chha jaata hai.",
    },
    "derivative": {
        "plain": "Derivative batata hai: input ko thoda hilaun to output kitna hilega? Gradient ye jawab ek saath har input ke liye deta hai, isliye wo chadhaai ki taraf point karta hai. Training gradient ke ulte chal kar neeche utarti hai. Chain rule hi wo cheez hai jo ye jawab layers ke poore stack me pahuchata hai.",
        "remember": "Central difference `(f(x+h)-f(x-h))/2h` haath se likhe gradient ko check karne ka sabse sasta tarika hai.",
        "mistake": "Aise derivation par bharosa karna jise aapne kabhi gradient-check nahi kiya; sign ki galti train dheere karti hai, saaf fail nahi hoti.",
    },
    "probability": {
        "plain": "Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.",
        "remember": "Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.",
        "mistake": "Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.",
    },
    "distribution": {
        "plain": "Distribution batati hai kaunsi values likely hain. Measurement noise ke liye Gaussian, haan/na ke liye Bernoulli, per-interval counts ke liye Poisson. Sahi distribution chunna hi apna loss function chunna hai: Gaussian likelihood se MSE aata hai, Bernoulli se cross-entropy.",
        "remember": "Jab result dobara banana ho to RNG hamesha seed karo (`default_rng(0)`).",
        "mistake": "Skewed, bounded ya count data par Gaussian maan lena aur phir residuals dekh kar hairan hona.",
    },
    "mean": {
        "plain": "Mean ko outliers kheench lete hain; median ko nahi. Dono report karo, saath me spread bhi. Jab mean aur median me bada farq ho to distribution skewed hai aur average aapse jhooth bol raha hai.",
        "remember": "Skewed data ke liye median + IQR batao, mean + std sirf roughly symmetric data ke liye.",
        "mistake": "'Outliers' ko apne aap hata dena jabki wahi events aapko predict karne ke liye rakha gaya tha.",
    },
    "hypothesis test": {
        "plain": "p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.",
        "remember": "Sample size aur metric data dekhne se PEHLE decide karo.",
        "mistake": "Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.",
    },
    "information theory": {
        "plain": "Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.",
        "remember": "`log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.",
        "mistake": "Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.",
    },
    "optimization theory": {
        "plain": "Convex loss ka ek hi neeche hota hai, to koi bhi dhalaan wahi pahucha degi. Neural network ka loss convex nahi hota — usme valleys, plateaus aur saddle points hote hain. High dimensions me saddle points asli local minima se kahin zyada milte hain, isiliye momentum wale optimisers itna madad karte hain.",
        "remember": "Agar loss oscillate ya explode kare, to sabse pehle learning rate aadha karo, baaki kuch badalne se pehle.",
        "mistake": "Architecture ko dosh dena jabki asli problem das guna bada learning rate hai.",
    },
    "supervised learning": {
        "plain": "Supervised learning jawab wale examples se mapping seekhta hai. Unsupervised bina jawab ke structure dhoondta hai. Reinforcement learning delayed reward se seekhta hai. Aaj bhi production ki zyadatar value simple supervised learning se hi aati hai, tabular data par.",
        "remember": "Pehle split karo, test set sabse aakhir me dekho. Har jhaank imaandaari kam karti hai.",
        "mistake": "Test set par bees models try karke model chunna — ab wo test score training score ban chuka hai.",
    },
    "linear regression": {
        "plain": "Linear regression squared error minimise karke seedhi line fit karta hai. Ye har regression problem ka imaandaar baseline hai: tez, samajhne layak, aur wahi cheez jise aapke fancy model ko harana padega tabhi wo apni complexity kamata hai.",
        "remember": "Predictions ke saamne residuals plot karo — koi bhi dikhne wala pattern matlab linear form galat hai.",
        "mistake": "Training data ka R² report karke use model performance bata dena.",
    },
    "logistic regression": {
        "plain": "Logistic regression linear score ko sigmoid se dabaa kar probability banata hai. Coefficients log-odds hain: +0.7 matlab odds lagbhag double. Jahan decision regulator ko samjhana pade, wahan aaj bhi yahi default hai.",
        "remember": "Sigmoid ka input clip karo — bade negative number ka `exp` overflow hokar NaN de deta hai.",
        "mistake": "Raw output ko calibrated probability maan lena bina kabhi calibration curve dekhe.",
    },
    "gradient descent": {
        "plain": "Gradient descent baar-baar gradient ke ulte kadam rakhta hai. Full-batch stable par dheema; stochastic shor wala par chhote gaddhon se nikal jaata hai; mini-batch practical beech ka raasta hai. Learning rate wo ek knob hai jise aap sabse zyada ghumaoge.",
        "remember": "Har epoch shuffle karo, warna model aapki file ka order seekh lega.",
        "mistake": "Learning rate ko hamesha fix rakhna, loss plateau hone par use decay na karna.",
    },
    "train test split": {
        "plain": "Teen split, teen kaam: train parameters fit karta hai, validation hyperparameters chunta hai, test ek imaandaar final number deta hai. K-fold cross-validation validation slice ghuma kar data dobara use karta hai — jab aapke paas kuch hazaar rows hi hon to ye zaroori hai.",
        "remember": "Folds ke beech ka spread bhi batao, sirf mean nahi — zyada variance matlab mean par bharosa mat karo.",
        "mistake": "Time-series ya grouped data (ek hi patient train aur test dono me) par random K-fold — dono leak karte hain.",
    },
    "overfitting": {
        "plain": "Underfitting matlab high bias: model itna simple hai ki har jagah galat hai, training data par bhi. Overfitting matlab high variance: usne training set ratt liya aur naye data par bikhar jaata hai. Train aur validation score ka farq batata hai aapke paas kaunsa wala hai.",
        "remember": "Train 1.00 / test 0.70 overfitting hai. Train 0.70 / test 0.69 underfitting hai. Sahi wale ko theek karo.",
        "mistake": "Capacity badha kar aisa gap theek karna jo asal me kam data ya leak se aaya tha.",
    },
    "regularization": {
        "plain": "Regularisation bade weights par penalty lagata hai taaki model simple explanation pasand kare. L2 (ridge) sab kuch smoothly chhota karta hai; L1 (lasso) kuch weights ko bilkul zero kar deta hai aur isi tarah features chunta hai. Elastic net dono milata hai.",
        "remember": "Regularise karne se pehle features scale karo, warna penalty usi column ko sazaa deta hai jiski units chhoti hain.",
        "mistake": "Test set par `alpha` tune karna — use sirf train par cross-validation se chuno.",
    },
    "feature scaling": {
        "plain": "Distance aur gradient wale models units ki parwah karte hain: rupaye wala salary column sirf magnitude se age column par chha jaayega. Zyadatar models ke liye standardise karo (mean 0, std 1); bounded [0,1] chahiye to min-max. Tree models ko koi farq nahi padta.",
        "remember": "Scaler ko Pipeline ke ANDAR rakho taaki cross-validation har fold me use dobara fit kare aur leak na ho.",
        "mistake": "Split se pehle poore dataset par `fit_transform` chala dena — classic, chupka, score badhaane wala leak.",
    },
    "categorical encoding": {
        "plain": "Models ko numbers chahiye. Kam-cardinality nominal categories ke liye one-hot safe hai. Label/ordinal encoding jhootha order bana deta hai, jab tak order asli na ho (small < medium < large). Target encoding powerful hai aur bura leak karta hai jab tak use cross-validation folds ke andar fit na kiya jaaye.",
        "remember": "Inference par unseen categories handle karo — pehle hi decide karo ki wo 'other' banengi ya error.",
        "mistake": "50,000 values wale ID column ko one-hot karke memory uda dena, bina kisi signal ke.",
    },
    "feature engineering": {
        "plain": "Feature engineering wahi jagah hai jahan domain knowledge compute ko harati hai. Ek ratio, ek lag, ek time-since-last-event, ya window par count aksar algorithm badalne se zyada deta hai. Selection phir un features ko hata deta hai jo signal ke bina variance badhate hain.",
        "remember": "Har banaya hua feature prediction ke waqt us data se calculate hona chahiye jo tab sach me maujood hoga.",
        "mistake": "Aise column se feature banana jo us event ke BAAD hi bharta hai jise aap predict kar rahe ho.",
    },
    "data leakage": {
        "plain": "Leakage matlab training me aisi information jo prediction ke waqt hogi hi nahi. Isse namumkin validation scores aate hain aur model production me dhah jaata hai. Agar accuracy shak ke laayak chhalaang lagaye, to jashn se pehle leak dhoondho.",
        "remember": "Mushkil business problem par 0.999 AUC ek bug report hai, result nahi.",
        "mistake": "Leaked model ship karke asli accuracy gusse wale users se pata chalna.",
    },
    "decision tree": {
        "plain": "Tree haan/na sawaal poochta hai aur split karke har taraf ko purer banata hai. Isse scaling nahi chahiye, ye mixed types sambhal leta hai, aur flowchart jaisa padhta hai. Bina rok-tok chhod do to ye training set ko poora ratt leta hai, isliye depth aur leaf-size limits zaroori hain.",
        "remember": "Ek bina-prune ka tree lagbhag hamesha chhote forest se kharab hota hai — par wo padha ja sakta hai, jo kabhi-kabhi jeet jaata hai.",
        "mistake": "Gehre tree ke feature importances par bharosa karna; wo unstable hain aur high-cardinality columns ki taraf jhukte hain.",
    },
    "random forest": {
        "plain": "Bagging bahut saare trees ko bootstrap samples aur random feature subsets par train karke average kar leta hai. Averaging wo variance kaat deta hai jo single trees ko unpredictable banata hai. Tabular data par jab bina tuning ke kuch chalta hua chahiye, random forest best default hai.",
        "remember": "Zyada trees kabhi overfit nahi karte — sirf time lagta hai. Depth aur leaf size hi fit control karte hain.",
        "mistake": "Business decisions ke liye impurity-based importances use karna, permutation importance ke bajaye.",
    },
    "gradient boosting": {
        "plain": "Boosting trees ko ek ke baad ek train karta hai, har naya pichhle ensemble ki galtiyan sudharta hai. Tabular data par ye aksar random forest se aage nikalta hai aur wahan aaj bhi deep learning ko harata hai. Keemat ye hai ki ise sach me tuning chahiye aur zyada chalne do to overfit kar dega.",
        "remember": "Kam learning rate + zyada trees + early stopping, ye zyada learning rate + kam trees se behtar hai.",
        "mistake": "Fix 1000 rounds bina early stopping chalana aur overfit ensemble ship kar dena.",
    },
    "knn": {
        "plain": "kNN me training step hota hi nahi: ye data rakh leta hai aur prediction ke waqt k sabse paas ke points me vote karwa leta hai. Ye ek badhiya sanity baseline hai, aur vector database bhi retrieval ke liye literally yahi karta hai — samajhna do baar kaam aata hai.",
        "remember": "Pehle features scale karo — kNN sirf distance hai, to units hi jawab tay karti hain.",
        "mistake": "High-dimensional data par kNN, jahan har point har doosre point se lagbhag barabar door hota hai.",
    },
    "svm": {
        "plain": "SVM classes ke beech sabse chaudi margin wali boundary dhoondta hai. Kernel trick use tedhi boundaries khinchne deta hai, higher-dimensional space me inner products nikaal kar, bina wo space kabhi banaye. Chhote, saaf, high-dimensional datasets (jaise text) par strong.",
        "remember": "SVM rows ke saath lagbhag quadratically badhta hai — ~100k samples se upar boosting uthao.",
        "mistake": "Feature scaling chhod dena, jo chupke se RBF kernel barbaad kar deta hai.",
    },
    "naive bayes": {
        "plain": "Naive Bayes maan leta hai ki class ke diye hue features independent hain. Ye assumption lagbhag hamesha jhooth hai, aur classifier phir bhi kaam karta hai — khaaskar text par. Ye ek hi pass me train hota hai, isliye 30-second baseline ke liye behtareen hai.",
        "remember": "Smoothing (alpha>0) use karo taaki koi unseen word poore product ko zero na kar de.",
        "mistake": "Naive Bayes ki probability outputs ko calibrated maan lena — wo mashhoor tor par overconfident hain.",
    },
    "clustering": {
        "plain": "Clustering bina labels ke points ko group karta hai. K-means se aapko k chunna padta hai aur ye gol, ek jaise size ke blobs maan leta hai. DBSCAN kisi bhi shape ke clusters dhoondta hai aur noise mark karta hai par density radius maangta hai. Clusters ko hamesha kisi aisi cheez se validate karo jise aap samajhte ho — clustering shor me bhi khushi se structure bana degi.",
        "remember": "Silhouette 1 ke paas matlab tight, alag-alag clusters; 0 ke paas matlab boundaries bemaani hain.",
        "mistake": "Cluster IDs ko matlab wale labels samajh lena — wo arbitrary hain aur har run me badal jaate hain.",
    },
    "pca": {
        "plain": "PCA data ko maximum variance wali axes par ghuma deta hai aur baaki chhodne deta hai. Ye linear, tez aur reversible hai. t-SNE aur UMAP sirf visualisation ke liye hain — t-SNE plot me clusters ke beech ki doori ka koi matlab nahi, isliye t-SNE output kabhi model me mat daalo.",
        "remember": "`n_components=0.95` PCA ko khud variance target se count chunne deta hai.",
        "mistake": "Scaling se pehle PCA chalana, jisse ek chaude range wala column akela component 1 ban jaata hai.",
    },
    "classification metric": {
        "plain": "Imbalanced data par accuracy sab chhupa leti hai. Precision poochti hai 'jinhe maine flag kiya unme se kitne asli the'; recall poochti hai 'jo asli the unme se kitne maine pakde'. Threshold se aap ek ko doosre ke badle bechte ho, aur kaunsi galti zyada mehngi hai ye business tay karta hai.",
        "remember": "Decision threshold validation data par tune karo; 0.5 ek default hai, decision nahi.",
        "mistake": "Bhaari imbalanced problem par ROC-AUC optimise karna jahan imaandaar metric precision-recall AUC hai.",
    },
    "regression metric": {
        "plain": "RMSE badi galtiyon ko quadratically sazaa deta hai; MAE har rupaye ki galti ko barabar maanta hai. R² batata hai ki mean predict karne ke muqable aapne variance ka kitna hissa samjhaya. Wo metric chuno jo aapke domain me galat hone ki keemat se match kare.",
        "remember": "Hamesha sabse bewakoof baseline se compare karo: mean predict karna, ya kal ki value predict karna.",
        "mistake": "Zero wale data par MAPE report karna — wo zero se divide karke infinity de deta hai.",
    },
    "imbalanced": {
        "plain": "Jab ek class data ka 1% ho, model hamesha 'no' bolna seekh leta hai. Ise class weights (sasta, pehli choice), threshold tuning, ya resampling se theek karo. SMOTE minority points banata hai — aur use sirf training fold par hi lagana chahiye.",
        "remember": "Kuch bhi install karne se pehle `class_weight='balanced'` try karo.",
        "mistake": "Split se pehle SMOTE lagana, jisse test rows ki synthetic copies training me aa jaati hain.",
    },
    "hyperparameter": {
        "plain": "Hyperparameters wo settings hain jo aap chunte ho, seekhi nahi jaatin. Grid search poora chhaanta hai aur barbaad karta hai; random search high dimensions me acche ilaake jaldi dhoondta hai; Bayesian search pichhle trials se seekhta hai. Search hamesha cross-validation ke andar karo.",
        "remember": "Random seed fix karo aur har trial log karo, warna aap apna hi best model dobara nahi bana paoge.",
        "mistake": "400 rows par 40 hyperparameters tune karna — ab aap validation set hi fit kar rahe ho.",
    },
    "pipeline": {
        "plain": "Pipeline preprocessing aur model ko ek hi object me jod deta hai jo ek unit ki tarah fit aur predict karta hai. Leakage ke khilaaf yahi sabse achhi dhaal hai, aur deployment ko chhe alag steps ke bajaye ek artefact milta hai jise yaad rakhne ki zaroorat nahi.",
        "remember": "`handle_unknown='ignore'` production ko us category par crash hone se bachata hai jo training me kabhi nahi dikhi.",
        "mistake": "Notebook me preprocess karna aur serving code likhte waqt ek step bhool jaana.",
    },
    "model persistence": {
        "plain": "Poori pipeline save karo, sirf estimator nahi. Library versions aur training data ka hash bhi save karo — alag scikit-learn version ka pickle load to ho jaayega par thoda alag numbers de sakta hai, jo fail hone se bhi bura hai.",
        "remember": "Aisi model file kabhi unpickle mat karo jo aapne nahi banayi — pickle load par arbitrary code chalata hai.",
        "mistake": "Bina version metadata ke pickle ship karna aur chhe mahine baad drift pata chalna.",
    },
    "perceptron": {
        "plain": "Ek neuron `activation(w·x + b)` nikaalta hai. Inhe layers me stack karo aur aap koi bhi continuous function approximate kar sakte ho. Non-linear activation ke bina das stacked layers algebra me ek hi linear layer ban jaati hain — non-linearity hi poora point hai.",
        "remember": "Bina non-linearity ke depth sirf width hai. Check karo ki har hidden layer par activation lagi hai.",
        "mistake": "Saare weights zero se shuru karna, jisse har neuron ko ek jaisa gradient milta hai aur sab ek hi cheez seekhte hain.",
    },
    "backpropagation": {
        "plain": "Backpropagation computation graph me ulta chain rule hai, jo intermediate results dobara use karta hai isliye cost lagbhag ek extra forward pass jitna hi hai. Har framework ye aapke liye karta hai — par ek baar haath se likhna hi failure modes ko padhne layak banata hai.",
        "remember": "Haath se likhe backward pass ko bharosa karne se pehle numeric estimate se gradient-check karo.",
        "mistake": "Steps ke beech gradients zero karna bhool jaana, jisse wo jud kar model ko diverge kar dete hain.",
    },
    "activation function": {
        "plain": "ReLU default hai: sasta, aur positive inputs par saturate nahi hota. Sigmoid aur tanh fixed range me dabate hain aur extremes par gradients maar dete hain. GELU/SiLU smooth ReLU hain jo transformers me use hote hain. Softmax scores ke vector ko probability distribution bana deta hai.",
        "remember": "Softmax me `exp` se pehle hamesha max ghatao, warna bade logits inf/NaN me overflow kar jaate hain.",
        "mistake": "Aakhri layer par softmax lagana AUR aisa loss use karna jo andar khud softmax lagata hai.",
    },
    "optimizer": {
        "plain": "SGD with momentum dhalaan ka raasta smooth karta hai. Adam har parameter ka step size adapt karta hai aur safe default hai. AdamW weight decay ko adaptive step se alag kar deta hai, isiliye har modern transformer wahi use karta hai. Warmup phir cosine decay standard recipe hai.",
        "remember": "Scratch training ke liye Adam ka default lr 1e-3 accha start hai; fine-tuning ke liye 1e-5 se 5e-5.",
        "mistake": "Pretraining aur fine-tuning me ek hi learning rate use karke pretrained weights barbaad kar dena.",
    },
    "vanishing gradient": {
        "plain": "Bahut saare chhote derivatives multiply hone se gradients gayab ho jaate hain; bade se explode. Residual connections gradient ko wapas jaane ka seedha raasta dete hain, isiliye 100-layer networks trainable bane. Clipping update norm ko cap karta hai taaki ek kharab batch weights uda na de.",
        "remember": "Training ke dauraan gradient norm log karo — achanak spike achanak loss spike ko samjha deta hai.",
        "mistake": "Architecture badalne ke peeche bhaagna jab `clip_grad_norm_(1.0)` hi instability theek kar deta.",
    },
    "batch normalization": {
        "plain": "Normalisation layers activations ko stable scale par rakhti hain taaki training atke nahi. BatchNorm batch ke aar-paar normalise karta hai (CNNs ke liye badhiya, chhote batches aur sequences ke liye ajeeb). LayerNorm har sample ke features ke aar-paar normalise karta hai, isiliye transformers wahi use karte hain.",
        "remember": "BatchNorm train aur eval mode me alag behave karta hai — `model.eval()` bhoolna inference kharab kar deta hai.",
        "mistake": "Batch size 2 par BatchNorm use karna, jahan batch statistics sirf shor hain.",
    },
    "dropout": {
        "plain": "Dropout training ke dauraan random activations zero kar deta hai taaki network kisi ek raaste par nirbhar na rahe. Early stopping tab rok deta hai jab validation loss sudharna band kar de. Augmentation aapke paas jo hai usi se aur training data bana leta hai — vision me teeno me sabse zyada return isi ka hai.",
        "remember": "Inverted dropout training ke waqt scale kar deta hai, isliye inference me kuch badalna nahi padta.",
        "mistake": "Inference par dropout chalu chhod dena aur har call par alag predictions paana.",
    },
    "pytorch": {
        "plain": "PyTorch matlab NumPy + gradients + GPU. Training loop hamesha wahi paanch lines hai: zero grads, forward, loss, backward, step. Ek baar haath se likh lo — har framework wrapper inhi paanch ko chhupa raha hota hai.",
        "remember": "Har step me pehle `opt.zero_grad()`. PyTorch design se hi gradients jodta hai.",
        "mistake": "`retain_graph` ke bina `loss.backward()` do baar call karna aur confusing runtime error paana.",
    },
    "vs gpu": {
        "plain": "GPU isliye jeette hain kyunki wo hazaaron multiply-add saath karte hain. Model aur data ek hi device par hone chahiye warna error. Mixed precision (bf16/fp16) memory aadhi kar deta hai aur modern cards par throughput lagbhag double, accuracy me lagbhag kuch kharcha kiye bina.",
        "remember": "CUDA OOM par sabse pehle batch size ghatao; effective batch banaye rakhne ke liye gradient accumulation use karo.",
        "mistake": "Har step ka poora loss tensor list me rakhna — wo poora graph pakde rehta hai aur memory leak karta hai.",
    },
    "cnn": {
        "plain": "Convolution ek chhota seekha hua filter image par sarkata hai, isliye wahi edge detector frame me kahin bhi kaam karta hai. Yahi weight sharing wajah hai ki CNN ko dense net se kahin kam parameters chahiye. Pooling map chhota karta hai aur thodi translation tolerance deta hai.",
        "remember": "Output size = (in - kernel + 2*pad)/stride + 1. Jab layer jud na rahi ho to shapes print karo.",
        "mistake": "Channel dimension bhool jaana aur (H,W) dena jahan layer (N,C,H,W) maang rahi hai.",
    },
    "image classification": {
        "plain": "Lagbhag koi bhi vision model scratch se train nahi karta. Laakhon images par pretrained network lo, aakhri layer badlo, aur ya to backbone freeze karo (kam data) ya use kam learning rate par fine-tune karo (zyada data). Applied vision me yahi sabse zyada leverage wala trick hai.",
        "remember": "Wahi normalisation statistics use karo jinke saath pretrained model train hua tha.",
        "mistake": "Poora network 1e-3 par fine-tune karke wo sab bahaa dena jo ImageNet ne sikhaya tha.",
    },
    "object detection": {
        "plain": "Classification batati hai kya; detection batata hai kya aur kahan. Boxes ko IoU (intersection over union) se score kiya jaata hai aur duplicates non-maximum suppression se hataye jaate hain. Segmentation isse aage ja kar har pixel ko label karta hai.",
        "remember": "IoU >= 0.5 aam 'sahi detection' threshold hai; accuracy nahi, mAP report karo.",
        "mistake": "Model aur evaluation code ke beech box formats mila dena (xywh vs xyxy).",
    },
    "rnn": {
        "plain": "RNN hidden state ko sequence ke saath aage le jaata hai, isliye order maayne rakhta hai. Simple RNNs jaldi bhool jaate hain kyunki gradients lambi doori par gayab ho jaate hain; LSTM aur GRU gates jodte hain jo information ko kai steps tak bina badle bahne dete hain. Transformers ne inhe kaafi had tak replace kar diya, par state aur memory ki intuition aaj bhi kaam ki hai.",
        "remember": "RNNs sequential hain — wo time ke aar-paar parallel nahi ho sakte, isiliye transformers jeet gaye.",
        "mistake": "Bina padding masks ke variable-length sequences dena, jisse padding tokens state ganda kar dete hain.",
    },
    "tokenization": {
        "plain": "Models text nahi, token IDs dekhte hain. Byte-pair encoding aksar aane wale character pairs ko jod deta hai taaki common words ek token banein aur rare words tukdon me toote. Tokens hi wajah hain ki bill per-token hai, context limits tokens me hain, aur models letters ginne me kamzor hain.",
        "remember": "Lagbhag 1 token ~ 4 English characters; doosri bhashaon me per word tokens kahin zyada lagte hain.",
        "mistake": "Cost ya context ka andaaza words me lagana, tokens me nahi, aur production me window overflow kar dena.",
    },
    "bag of words": {
        "plain": "Embeddings se pehle text ginti se numbers banta tha. TF-IDF ek word ko is hisaab se weight deta hai ki wo yahan kitni baar aaya aur overall kitna rare hai, isliye 'the' ka score lagbhag zero ho jaata hai. Classification aur keyword search ke liye ye aaj bhi lagbhag muft ka behtareen baseline hai.",
        "remember": "TF-IDF + logistic regression wo baseline hai jise har LLM text classifier ko harana padega tabhi wo apni cost layak hai.",
        "mistake": "Support tickets classify karne ke liye 7B model uthana jab TF-IDF muft me 94% de deta hai.",
    },
    "embedding": {
        "plain": "Embedding text ko dense vector me badalta hai jahan paas hona matlab matlab me paas hona. Keyword search ke ulat, 'car trouble' 'engine won't start' se match ho jaata hai. Har RAG system embeddings + nearest-neighbour lookup hi hai.",
        "remember": "Embeddings normalise kar do, phir cosine similarity sirf dot product hai — scale par bahut tez.",
        "mistake": "Ek hi index me do alag embedding models ke vectors mila dena; wo spaces aapas me bilkul unrelated hain.",
    },
    "attention": {
        "plain": "Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.",
        "remember": "1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.",
        "mistake": "Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.",
    },
    "transformer": {
        "plain": "Transformer block = attention + feed-forward, dono residual connection aur LayerNorm me lipte hue. Akeli attention order-blind hai, isliye positions alag se daali jaati hain. Encoder-only (BERT) samajhne ke liye, decoder-only (GPT) generation ke liye, encoder-decoder (T5) translation jaise tasks ke liye.",
        "remember": "Block = LayerNorm -> Attention -> residual add -> LayerNorm -> MLP -> residual add. Ise ratt lo.",
        "mistake": "Yeh maan lena ki bada context window muft hai — attention ka cost sequence length ke square se badhta hai.",
    },
    "pretraining": {
        "plain": "Pretraining ek behad simple objective hai bade paimane par: agla token predict karo. Baaki sab — grammar, facts, reasoning, style — trillions tokens par ise achhe se karne se hi nikal aata hai. Scaling laws kehte hain ki model size, data aur compute saath badhne par loss predictably girta hai.",
        "remember": "Bahut kam data par bada model barbaadi hai — compute, parameters aur tokens saath scale hote hain.",
        "mistake": "Ye maanna ki base model instructions follow karega; wo behaviour baad ke tuning stages se aata hai.",
    },
    "fine-tuning": {
        "plain": "Fine-tuning pretrained model ko aapke examples par aur train karta hai. Ye format, tone aur task ki shape naye facts se kahin behtar sikhata hai — facts ke liye retrieval use karo. Kuch sau behtareen examples aksar das hazaar aam examples se behtar hote hain.",
        "remember": "Behaviour aur format ke liye fine-tune karo. Jo knowledge badalti rehti hai uske liye RAG.",
        "mistake": "Company facts daalne ke liye fine-tune karna, phir har policy document badalne par dobara train karna.",
    },
    "lora": {
        "plain": "LoRA base weights freeze kar deta hai aur do chhoti low-rank matrices train karta hai jinka product har target layer me joda jaata hai. Aap ~0.1% parameters update karte ho, checkpoint gigabytes ke bajaye megabytes ka hota hai, aur har customer ke liye adapter badla ja sakta hai. QLoRA 4-bit base weights jodta hai taaki 7B model ek consumer GPU par aa jaaye.",
        "remember": "B ko zeros se initialise karo taaki adapted model bilkul base model ke barabar shuru ho.",
        "mistake": "Rank bahut zyada rakh dena — efficiency chali jaati hai aur overfitting aa jaati hai.",
    },
    "rlhf": {
        "plain": "Supervised tuning ke baad models human preference se align kiye jaate hain. RLHF human comparisons par reward model train karta hai, phir PPO se uske khilaaf optimise karta hai. DPO reward model chhod kar seedhe preference pairs optimise karta hai — simple, sasta, aur ab aam choice.",
        "remember": "Alignment us cheez ka proxy optimise karta hai jo insaan chahte hain; proxy hamesha game kiya ja sakta hai.",
        "mistake": "Reward model ko itna over-optimise kar dena ki outputs chaploos aur bekaar ho jaayein — classic reward hacking.",
    },
    "prompt engineering": {
        "plain": "Prompt English me likha gaya program hai. Role, task, format aur constraints ke baare me specific raho. Few-shot examples format kisi bhi description se behtar sikhaate hain. Reasoning steps maangna multi-step problems par madad karta hai aur simple lookups par tokens barbaad karta hai.",
        "remember": "Output format sabse aakhir me rakho aur use example ki tarah dikhao — models sabse paas wala pattern copy karte hain.",
        "mistake": "Dhundhla prompt likhna, dhundhla output paana, aur model ko dosh dena.",
    },
    "structured output": {
        "plain": "Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.",
        "remember": "Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.",
        "mistake": "Model output ko seedha `eval`, shell command, ya SQL string me daal dena.",
    },
    "rag": {
        "plain": "RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.",
        "remember": "Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.",
        "mistake": "Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.",
    },
    "agent": {
        "plain": "Agent ek loop hai: model tool chunta hai, aapka code use chalata hai, result wapas context me jaata hai, aur ye dohraata hai jab tak kaam poora na ho. Taakat tools se aati hai, prompt se nahi. Iterations cap karo, har step log karo, aur kisi bhi irreversible cheez se pehle confirmation maango.",
        "remember": "Loop hamesha bounded rakho. Bina limit ka agent paisa jalata hai aur fail hone ke naye tareeke dhoondh leta hai.",
        "mistake": "Agent ko shell tool dena bina allowlist aur bina confirmation step ke.",
    },
    "prompt injection": {
        "plain": "Retrieved documents, web pages aur user files untrusted input hain. Agar aapka prompt inhe jod deta hai, to attacker PDF me 'ignore previous instructions' likh kar aapke agent ko steer kar sakta hai. Model output ko bhi untrusted maano, aur permission checks code me rakho, prompt me nahi.",
        "remember": "Untrusted content ko delimit karo aur authorisation code me lagu karo — prompt security boundary nahi hai.",
        "mistake": "Model ke chune hue tool call ko caller ki poori privileges ke saath bina allowlist chalne dena.",
    },
    "hallucination": {
        "plain": "Language model plausible tokens predict karta hai, sach wale nahi. Fluent aur galat uska default failure mode hai. Ise kam karo jawaabon ko retrieved sources me ground karke, citations maang kar, 'mujhe nahi pata' ki ijaazat de kar, aur mehnge claims verify karke.",
        "remember": "Ek saaf 'mere sources me nahi hai' wala raasta kisi bhi confidence score se zyada keemti hai.",
        "mistake": "Bina abstain path ke chatbot ship karna, jo dabaav me policy khud gadh leta hai.",
    },
    "llm evaluation": {
        "plain": "Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.",
        "remember": "Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.",
        "mistake": "Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.",
    },
    "context window": {
        "plain": "Temperature 0 lagbhag deterministic hai aur extraction ke liye sahi; zyada values creative kaam ke liye variety deti hain. Top-p sabse chhota set rakhta hai jo probability mass ka p cover kare. Cost per token in aur out hai, isliye prompt chhota karna sabse sasta optimisation hai.",
        "remember": "Jise aap parse karoge uske liye temperature 0 use karo; randomness prose ke liye bachaao.",
        "mistake": "Temperature 1 par extraction chala kar hafte bhar 'random' JSON failures debug karna.",
    },
    "claude api": {
        "plain": "Messages API ek system prompt plus alternating user/assistant turns leta hai aur content blocks lautata hai. Stable content (lambi instructions, retrieved corpora) shuru me rakho aur use cacheable mark karo — cache hits latency aur cost dono kaafi kam kar dete hain. Jab insaan intezaar kar raha ho to stream karo.",
        "remember": "API key kabhi hard-code mat karo. Use environment se padho aur git se door rakho.",
        "mistake": "Har call me prompt ka order badalna, jisse cache kabhi hit hi nahi hota.",
    },
    "autoencoder": {
        "plain": "Autoencoder input ko ek patli bottleneck se nichodta hai aur wapas banata hai, jisse ek compact representation banna majboori ho jaati hai. VAE us bottleneck ko distribution bana deta hai taaki aap usse naya data sample kar sako. Dono anomaly detection ke liye kaam ke hain: zyada reconstruction error matlab 'jaisa maine train kiya usse alag'.",
        "remember": "Reconstruction error khud hi ek anomaly score hai — labels ki zaroorat hi nahi.",
        "mistake": "Bottleneck ko input jitna hi chauda kar dena, jisse network sirf identity function seekh leta hai.",
    },
    "gan": {
        "plain": "GAN generator ko discriminator ke khilaaf khada karta hai: ek nakli data banata hai, doosra nakli pakadta hai, aur dono behtar hote hain. Training mashhoor tor par unstable hai — mode collapse matlab generator ko ek convincing output mil gaya aur usne khojna band kar diya. Images ke liye diffusion ne GANs ko kaafi had tak replace kar diya.",
        "remember": "Loss curves nahi, samples dekho — GAN losses progress ka signal nahi hain.",
        "mistake": "Discriminator ko bahut jaldi bahut strong hone dena, jisse generator ko gradient hi nahi milta.",
    },
    "diffusion": {
        "plain": "Diffusion noise ulta karna seekhta hai: images me chhote steps me Gaussian noise daalo, phir network ko ek step wapas karna sikhao. Generation me aap pure noise se shuru karke baar-baar denoise karte ho, text embedding ke ishaare par. Ye GAN training se zyada stable hai aur ab images ka default hai.",
        "remember": "Zyada sampling steps matlab behtar quality aur usi hisaab se zyada compute — bas yahi poora sauda hai.",
        "mistake": "Ye maan lena ki generated images copyright ya bias se aazad hain kyunki 'model ne banayi hai'.",
    },
    "speech": {
        "plain": "Audio spectrogram ban jaata hai — ek axis par time, doosri par frequency — aur uske baad ye image problem hi hai. ASR speech ko text me badalta hai; TTS ulta karta hai. Training data me accent aur background-noise bias par nazar rakho.",
        "remember": "Inference se pehle sab kuch model ke expected sample rate par resample karo.",
        "mistake": "ASR ko sirf saaf studio audio par evaluate karna, phir shor wale call centre me deploy kar dena.",
    },
    "multimodal": {
        "plain": "Multimodal models images aur text ko ek hi shared embedding space me daal dete hain, isliye kutte ki photo 'a dog' shabdon ke paas girti hai. Isi ek trick se aapko zero-shot classification, description se image search, aur captioning mil jaate hain — bina kisi task-specific training ke.",
        "remember": "Zero-shot quality prompt ki wording par bahut depend karti hai — 'a photo of a {}' saade noun se behtar hai.",
        "mistake": "Image ko galat resolution ya normalisation par dena aur chupchap quality khona.",
    },
    "reinforcement learning": {
        "plain": "RL labels ke bajaye reward se seekhta hai. Agent actions leta hai, environment state aur reward lautata hai, aur agent aisi policy seekhta hai jo long-term return maximise kare. Mushkil hissa exploration vs exploitation hai aur ye ki reward delayed aur sparse hota hai.",
        "remember": "Reward shaping hi tay karta hai ki agent asal me kya seekhega — aur wo har chhod ka faayda uthaega.",
        "mistake": "Proxy metric par reward dena aur aisa agent paana jo proxy maximise karta hai par asli goal fail karta hai.",
    },
    "time series": {
        "plain": "Time series wo i.i.d. assumption todti hain jis par baaki har model tika hai. Aapko time se split karna hi padega, random se kabhi nahi. Zyadatar value lag features, rolling statistics aur calendar effects se aati hai — aksar upar se saada gradient boosting laga kar.",
        "remember": "Har feature `.shift(1)` ya usse aage ka use kare — koi row apna khud ka future na dekhe.",
        "mistake": "Aisa rolling mean jo current row ko bhi shaamil kare, jo target ko feature me leak kar deta hai.",
    },
    "recommender": {
        "plain": "Collaborative filtering kehta hai: jinhe wo pasand aaya jo aapko pasand aaya, unhe X bhi pasand aaya. Matrix factorisation latent user aur item vectors seekhta hai jinka dot product rating predict karta hai. Cold-start problem — naye users aur naye items bina history ke — content features se hal hoti hai, aur factorisation se nahi.",
        "remember": "Recommenders ko ranking metrics (precision@k, NDCG) se evaluate karo, ratings par RMSE se nahi.",
        "mistake": "Aisa feedback loop banana jo hamesha wahi recommend karta hai jo pehle se recommend kar raha tha.",
    },
    "graph neural": {
        "plain": "GNN edges ke saath messages bhejta hai: har node apne padosiyon se khud ko update karta hai, k baar, taaki information k hops tak safar kare. Fraud rings, molecules aur social graphs ke liye badhiya — jahan bhi rishte nodes se zyada signal rakhte hain.",
        "remember": "Bahut zyada message-passing layers over-smoothing kar deti hain — har node ek jaisa vector ban jaata hai.",
        "mistake": "Graph data ko randomly split karna, jisse ek node ke apne padosi train aur test dono me aa jaate hain.",
    },
    "explainability": {
        "plain": "Agar aap decision samjha nahi sakte, to aap use defend bhi nahi kar sakte — aur credit, hiring aur healthcare me ye legally zaroori hai. Permutation importance model-agnostic aur imaandaar hai. SHAP per-prediction attributions deta hai theoretical base ke saath par sach me compute maangta hai.",
        "remember": "TEST set par permutation importance batati hai ki generalise karne ke liye model kis par tik raha hai.",
        "mistake": "Importance ko causation ki tarah pesh karna — model ne correlation dhoonda hai, bas.",
    },
    "fairness": {
        "plain": "Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.",
        "remember": "Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.",
        "mistake": "Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.",
    },
    "fastapi": {
        "plain": "Model serve karna matlab use startup par ek baar load karna aur HTTP requests ka jawab dena. Input schema validate karo, errors structured JSON me lautao, health endpoint jodo, aur model ko request handler ke andar kabhi load mat karo.",
        "remember": "Jahan latency ijaazat de wahan requests batch karo — batch size 1 par GPU throughput dhah jaata hai.",
        "mistake": "Har request par model dobara load karna aur sochna ki p99 latency chaar second kyun hai.",
    },
    "docker": {
        "plain": "Container code, dependencies aur interpreter ko package kar deta hai taaki har jagah ek jaisa chale. Versions pin karo, slim base use karo, aur bade model weights image layer se bahar rakho — unhe mount ya download karo.",
        "remember": "`--no-cache-dir` aur slim base images chhoti rakhte hain; chhoti images tez deploy hoti hain.",
        "mistake": "`pip install` se pehle `COPY . .` likhna, jisse har code edit par dependency cache toot jaata hai.",
    },
    "mlops": {
        "plain": "Jo experiment aap dobara nahi bana sakte wo kissa hai. Har run ke liye track karo: code commit, data version, hyperparameters, metrics aur artefact. Chhe mahine baad 'production wala model kis run se aaya' ka jawab hona hi chahiye.",
        "remember": "Code version ke saath data version bhi log karo — data chupchap badalta hai, code shor machaa kar.",
        "mistake": "Registry use karne ke bajaye files ko `model_final_v2_REAL_use_this.pkl` naam dena.",
    },
    "monitoring": {
        "plain": "Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.",
        "remember": "PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.",
        "mistake": "Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.",
    },
    "testing ml": {
        "plain": "ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.",
        "remember": "Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.",
        "mistake": "Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.",
    },
    "scaling": {
        "plain": "Data parallelism model ki copies banata hai aur batch baant deta hai; model parallelism model ko baantta hai jab wo ek device par na aaye. Profiling ke baad hi scale karo — 'humein aur GPUs chahiye' wali zyadatar problems asal me dheema data loader hoti hain.",
        "remember": "Pehle profile karo. GPU 30% utilisation par matlab bottleneck data pipeline hai, GPU nahi.",
        "mistake": "Batch scale karte waqt learning rate galat scale karna — bade batch ko aam taur par bada LR chahiye.",
    },
    "project": {
        "plain": "Projects wahi jagah hain jahan seekha hua chipakta hai. Pehle ek patli end-to-end slice banao — data load, kuch bewakoof train, evaluate, ek prediction serve — phir ek-ek layer sudharo. Pehle din chalne wala baseline us perfect model se behtar hai jo kabhi ship hi nahi hota.",
        "remember": "Hyperparameters tune karne me ek din lagane se pehle galat predictions dekhne me ek ghanta lagao.",
        "mistake": "Chhe hafte feature engineering karna bina kisi baseline ke jo sabit kare ki kisi cheez se fayda hua.",
    },
    "career": {
        "plain": "Interviews me depth breadth se jeetti hai: ek project jise aap end-to-end defend kar sako — wo metric kyun, wo split kyun, kya fail hua — das tutorial notebooks se behtar hai. Papers ko three-pass method se padho: abstract aur figures, phir method, phir details sirf tab jab aap use implement karoge.",
        "remember": "Agar aap ye nahi samjha sakte ki aapka validation split imaandaar kyun hai, to project abhi aapka nahi hua.",
        "mistake": "CV par bees frameworks likhna aur kisi ek me bhi shape error debug na kar paana.",
    },

    # ---------------- gap-fill entries ----------------
    "why python owns ai": {
        "plain": "Python AI me isliye nahi jeeta ki wo tez hai, balki isliye ki tez hisse (NumPy, PyTorch) andar se C aur CUDA hain, upar se aisi bhasha me lipte hue jisme aap soch sakte ho. Aapka pehla kaam ek chalta hua, alag environment banana hai aur ye aadat daalna ki aap sach me kaunsa interpreter chala rahe ho — zyadatar 'meri machine par to chalta hai' wale bugs wahin se shuru hote hain.",
        "remember": "Ye file pehle din chalao aur jab bhi kuch rahasyamay toote — 'kaunsa Python?' ka jawab turant mil jaata hai.",
        "mistake": "Ek Python se package install karna aur doosre se import karna, phir package ko dosh dena.",
    },
    "pip install": {
        "plain": "`pip install X` aaj ka sabse naya compatible version uthaata hai, jo wo nahi hai jo aapke colleague ko pichhle mahine mila tha. `requirements.txt` me exact versions pin karo taaki result dobara ban sake. Install hamesha activated virtual environment me karo, globally kabhi nahi.",
        "remember": "`numpy>=1.26` ek khwaahish hai; `numpy==1.26.4` ek vaada hai. Jise dobara banana ho use exactly pin karo.",
        "mistake": "Requirements file ke bina code commit karna, jisse koi bhi wo environment dobara nahi bana sakta jisne aapke numbers diye the.",
    },
    "colab": {
        "plain": "Colab browser me muft GPU deta hai, jo deep learning shuru karne ki sabse badi rukaawat hata deta hai. Pech ye hai ki machine aarzi hai: kuch ghante idle rehne par gayab ho jaati hai aur aapki files bhi le jaati hai. Har baar Drive mount karo ya checkpoints kisi permanent jagah save karo.",
        "remember": "Jo /content ke bahar save nahi hai wo runtime recycle hote hi khatam. Har epoch checkpoint karo.",
        "mistake": "Colab me chaar ghante bina checkpointing train karna aur ek disconnect me sab kho dena.",
    },
    "vs code": {
        "plain": "Koi bhi editor chalta hai, par chaar cheezein asli waqt bachati hain: jump-to-definition, integrated debugger, interpreter selector, aur inline type errors. Debugger khaaskar seekho — shape mismatch me step karna bees `print` statements se hamesha behtar hai.",
        "remember": "`breakpoint()` built-in hai. Value dekhne ke liye ab kabhi print statements jodne ki zaroorat nahi.",
        "mistake": "Nested pipeline ko print statements se debug karna jinhe aap phir hataana bhool jaate ho.",
    },
    "dict and set comprehension": {
        "plain": "Ye wo tools hain jo haath se likhe loops ki jagah ek padhne layak line le lete hain. `Counter` ginta hai, `defaultdict` 'if key not in dict' wala natak hata deta hai, `sorted(key=...)` kisi bhi cheez se sort karta hai, aur `zip` do sequences ko saath chalata hai. Inhe uthana hi wo farq hai jo Python ko Python jaisa banata hai, translate kiye hue Java jaisa nahi.",
        "remember": "`Counter` aur `defaultdict` wo zyadatar bookkeeping code hata dete hain jo log haath se likhte hain.",
        "mistake": "Har script me hamesha ke liye `if k in d: d[k] += 1 else: d[k] = 1` se frequency counts banana.",
    },
    "mutable default": {
        "plain": "Default arguments ek hi baar evaluate hote hain, function define hone ke waqt. Isliye mutable default (list, dict, set) har call me share hota hai — ye bug aise dikhta hai ki 'mera function pichhli call yaad rakhta hai'. `None` use karo aur asli default andar banao.",
        "remember": "Default arguments immutable hone chahiye. `None` plus ek check hi standard fix hai.",
        "mistake": "Aisa `def f(x, cache={})` jo process ki har call me chupchap state jama karta rehta hai.",
    },
    "variables, types": {
        "plain": "Python types runtime par tay karta hai, jo likhne me tez hai aur chupke se galat karna aasan. Apne containers ki cost jaano: order ke liye list, membership ke liye set, keyed lookup ke liye dict. Truthiness `0`, `''`, `[]`, `{}` aur `None` ko false maanti hai — isiliye `if x:` aur `if x is not None:` alag sawaal hain.",
        "remember": "`if x:` aur `if x is not None:` 0, '' aur khaali containers par alag hain. Soch kar chuno.",
        "mistake": "Missing field check karne ke liye `if not value:` use karna aur ek jaayaz zero ko reject kar dena.",
    },
    "classes and instances": {
        "plain": "Class data ko un operations ke saath baandhti hai jo use valid rakhte hain. Saade config ya record objects ke liye `@dataclass` aapko `__init__`, `__repr__` aur `__eq__` muft de deta hai. Inheritance par composition prefer karo: gehre class trees badalna mushkil aur todna aasan hota hai.",
        "remember": "Dataclass me mutable defaults ko `field(default_factory=...)` chahiye, literal nahi.",
        "mistake": "Us cheez ke liye paanch-level inheritance banana jise ek dict aur do functions hal kar dete.",
    },
    "exception": {
        "plain": "Exceptions happy path ko failure handling se alag karte hain. Sabse sankeern exception pakdo jisse aap sach me ubhar sakte ho, baaki ko upar jaane do — khaali `except:` wahi bug chhupata hai jise dekhna sabse zaroori tha. Tracebacks neeche se upar padho: aakhri line batati hai kya toota, upar ki lines batati hain aap wahan pahuche kaise.",
        "remember": "`raise ... from e` asli wajah traceback me rakhta hai. Use kabhi nigalo mat.",
        "mistake": "Poore pipeline ke aas-paas `except: pass`, jo crash ko chupchap galat output me badal deta hai.",
    },
    "type hints": {
        "plain": "Type hints runtime behaviour nahi badalte; wo ye badalte hain ki koi insaan (ya checker) function ko kitni jaldi samajhta hai. Data pipeline me signature aisi documentation hai jo purani nahi ho sakti. Chhote functions aur imaandaar naamon ke saath milao aur zyadatar comments ki zaroorat hi nahi rahegi.",
        "remember": "Boundaries par hints do (function signatures, config objects); obvious locals par chhod do.",
        "mistake": "Har cheez par annotation lagana, throwaway locals par bhi, jab tak types logic se bhaari na ho jaayein.",
    },
    "reading and writing text files": {
        "plain": "`with open(...)` file band kar deta hai chahe body me exception aa jaaye — context manager isi ke liye hai. File object par line-by-line ghumo aur Python poori file memory me kabhi nahi laata, isi tarah laptop par 40 GB ka log process hota hai.",
        "remember": "Hamesha `encoding='utf-8'` explicitly do — Windows par platform default alag hota hai.",
        "mistake": "Badi file par `fh.read().split('\\n')`, jo sab RAM me laa kar mar jaata hai.",
    },
    "json serialization": {
        "plain": "JSON aapke code, APIs aur model outputs ke beech ki aam bhasha hai. `pathlib` paths ko Windows aur Linux dono par ek jaisa chalata hai. Secrets environment variables me rakho, source file me kabhi nahi — kyunki source file git me pahuchti hai, aur git hamesha ke liye yaad rakhta hai.",
        "remember": "Slashes wali string joduai ke bajaye `Path` division (`root / 'data' / 'x.csv'`) use karo.",
        "mistake": "API key commit karna, phir baad ke commit me 'hata dena' jabki wo history me abhi bhi zinda hai.",
    },
    "boolean masking": {
        "plain": "NumPy ki taakat bina loops ke select aur combine karna hai. Boolean mask condition se rows chunta hai, fancy indexing position se, `np.where` condition se naya array banata hai, aur `argsort` ordering deta hai taaki aap kai arrays ko ek hi tarah sort kar sako.",
        "remember": "Boolean mask copy lautata hai; saada slice view lautata hai. Ek ko badalna doosre par ek jaisa asar nahi karta.",
        "mistake": "`arr[mask][0] = 5` chain karna aur sochna ki original array kyun nahi badla — aapne copy par likha.",
    },
    "sql": {
        "plain": "Zyadatar production data database me hi rehta hai, aur ek average nikalne ke liye ek crore rows pandas me kheenchna har cheez ki barbaadi hai. SQL me aggregate karo, chhota result wapas lao. Window functions aapko lag features aur running totals database chhode bina de dete hain.",
        "remember": "Filtering aur aggregation SQL me dhakelo; sirf wahi lao jis par aap sach me model banaoge.",
        "mistake": "Chaudi table par `SELECT *`, phir pandas me 90% columns drop kar dena.",
    },
    "solving linear systems": {
        "plain": "`Ax = b` solve karne ke liye solver use karo, inverse nahi. `inv(A) @ b` dheema bhi hai aur numerically kharab bhi. Sparse matrices (zyadatar zeros — text features, graphs) ko sparse storage chahiye warna aap gigabytes zeros allocate kar doge.",
        "remember": "`inv(A) @ b` ke bajaye `np.linalg.solve(A, b)`, hamesha.",
        "mistake": "Sparse TF-IDF matrix ko `.toarray()` se dense banana aur memory khatam kar dena.",
    },
    "objective function": {
        "plain": "Optimisation matlab: objective define karo, direction nikaalo, kadam rakho, aur tay karo kab rukna hai. Second-order methods (Newton) kam steps me pahuchte hain par Hessian maangte hain, jo laakhon parameters par afford hi nahi hota. Fixed iteration count ke bajaye relative improvement threshold par ruko.",
        "remember": "Convergence par ruko, aur step count log karo — jo run max_steps tak pahuch gaya wo converge nahi hua.",
        "mistake": "Aise optimiser ka result batana jo chupchap apni iteration limit par ruk gaya tha.",
    },
    "population vs sample": {
        "plain": "Aap sample naapte ho aur population ke baare me daawa karna chahte ho. Type I error jhoothi cheekh hai; Type II asli effect chook jaana. Power ye chance hai ki aap di gayi size ka asli effect pakad paoge — ise data jama karne se pehle tay karo, warna aap aisa experiment chalaoge jo kabhi safal ho hi nahi sakta tha.",
        "remember": "20 hypotheses ko p<0.05 par test karne se average ek false positive milta hi hai. Uske liye correction karo.",
        "mistake": "Baad me data ko pandrah tarah se kaat kar wahi ek slice report karna jo significant nikla.",
    },
    "floating point representation": {
        "plain": "Floats approximations hain. Do lagbhag barabar numbers ghatane se precision khatm ho jaati hai; bade numbers ka exponent inf me overflow karta hai; bahut chhote number se divide karna phat jaata hai. Log-sum-exp trick aur denominator me chhota epsilon — yahi do fixes aap baar-baar use karoge.",
        "remember": "Floats ko tolerance se compare karo (`np.isclose`), `==` se kabhi nahi.",
        "mistake": "Training me gehre andar `nan` milna aur tab pata chalna ki baarah steps pehle ek `exp()` overflow ho gaya tha.",
    },
    "einsum": {
        "plain": "`einsum` tensor contractions ko index notation me likhta hai — transposes aur reshapes ki lambi chain se zyada saaf. float32 memory aadhi karta hai aur training ka standard hai; float64 un scientific kaamon ke liye hai jahan accumulation error maayne rakhta hai. Row-major layout matlab aakhri axis ke saath ghumna cache-friendly aur kaafi tez hai.",
        "remember": "float32 (ya bf16) me train karo; float64 sirf numerically nazuk accumulations ke liye bachao.",
        "mistake": "Galti se float32 aur float64 mila dena aur poore pipeline ki memory chupchap double kar dena.",
    },
    "big-o": {
        "plain": "Complexity architecture tay karti hai. Attention sequence length me quadratic hai, kNN har query par dataset size me linear, aur hash lookup constant. Kaunsa operation haavi hai ye jaan lene se pata chal jaata hai ki data das guna hone par sabse pehle kya tootega.",
        "remember": "Constants optimise karne se pehle check karo ki kahin aapne O(n log n) problem ke liye O(n^2) shape to nahi chun li.",
        "mistake": "Loop ke andar list par membership test, jo linear kaam ko quadratic bana deta hai.",
    },
    "euclidean and manhattan": {
        "plain": "Distance function hi aapki similarity ki definition hai. Euclidean maanta hai ki saare dimensions comparable hain, Manhattan single dimension ke outliers ke prati robust hai, Mahalanobis correlation ka hisaab rakhta hai, Jaccard sets compare karta hai, edit distance strings. High dimensions me saari Euclidean distances paas aa jaati hain — yahi curse hai.",
        "remember": "Dimensions badhne par distance ka spread/mean ratio ghatta hai — nearest neighbour ka matlab hi khatm hone lagta hai.",
        "mistake": "Bilkul alag units wale features par Euclidean distance use karna aur result ko similarity kehna.",
    },
    "choosing a target variable": {
        "plain": "Zyadatar fail hue ML projects modelling par nahi, framing par fail hue. Likh kar rakho: is prediction se kaunsa decision badlega, prediction ki unit kya hai, kaunsa metric safalta naapta hai, aur sabse bewakoof baseline kitna laata hai. Agar ek rule aapke model ko haraata hai, to rule hi ship karo.",
        "remember": "Features list karne se pehle likho ki *prediction ke waqt* kaunsa data maujood hoga. Wahi list zyadatar leaks maar deti hai.",
        "mistake": "Chhe hafte model banana aur phir pata chalna ki jo decision ye support karta hai wo pehle se automated hai.",
    },
    "public dataset": {
        "plain": "Data kahan se aaya ye tay karta hai ki aap uske saath kya kar sakte ho. Train karne se pehle licence check karo, personal identifiers shuru me hi hata ya hash kar do, aur provenance record karo taaki saal bhar baad 'ye row kahan se aayi' ka jawab de sako. Paginated APIs ko backoff aur idempotent resume chahiye.",
        "remember": "Identifiers ingestion par hash ya drop karo, report ke waqt nahi — tab tak copies ban chuki hoti hain.",
        "mistake": "Aise source ko scrape karna jiske terms mana karte hain, aur problem model production me jaane ke baad pata chalna.",
    },
    "train, validation and test roles": {
        "plain": "Train parameters fit karta hai, validation baaki sab chunta hai, test ek hi baar khulta hai. Classes imbalanced hon to stratify karo, ek hi entity baar-baar aaye to group karo, aur agar aap future predict kar rahe ho to time se split karo. Galat split uske baad ke har number ko bekaar kar deta hai.",
        "remember": "Ek entity split ke theek ek hi taraf honi chahiye. Overlap check karo, maan mat lo.",
        "mistake": "Repeated customers wale data par random split, jisse model customer ko pehchanta hai, pattern ko nahi.",
    },
    "schema as a contract": {
        "plain": "Data contract un assertions ka set hai jinke bina aapka pipeline chalne se mana kar de: columns maujood, types sahi, nulls threshold ke neeche, categories known set se, row count plausible range me. Ingestion par shor machaa kar fail hona ek chaupai bhar chupchap galat predictions se sasta hai.",
        "remember": "Wahi validation training AUR inference dono par chalao — dono ke beech ka skew top production failure hai.",
        "mistake": "Validation sirf training pipeline me rakhna, jisse production chupchap ek renamed, null se bhara column le leta hai.",
    },
    "fit, predict, score": {
        "plain": "Har scikit-learn model ke wahi teen methods hain, matlab algorithm badalna ek line ka kaam hai. Har problem `DummyClassifier` se shuru karo — agar aapka asli model 'hamesha majority class bolo' ko saaf farq se nahi haraata, to gadbad data me hai, model me nahi.",
        "remember": "Apne model ka score dummy ke score ke bagal me batao. Akela number kuch matlab nahi rakhta.",
        "mistake": "Aise data par 92% accuracy ka jashn manana jahan 91% rows ek hi class ki hain.",
    },
    "comparing models fairly": {
        "plain": "Do models jinme 0.3% ka farq hai aur folds ke beech 2% ka spread, wo ek hi model hain. Bilkul ek jaise folds par compare karo, spread dekho, aur score barabar hon to simple model lo — yahi one-standard-error rule hai. Jab aapne hyperparameters bhi tune kiye hon to imaandaar score batane ka tarika nested CV hai.",
        "remember": "Har candidate ke liye wahi `cv` object use karo, warna aap kismat compare kar rahe ho.",
        "mistake": "Folds ke standard error se chhote farq se vijeta ghoshit kar dena.",
    },
    "isolation forest": {
        "plain": "Anomaly detection matlab classification jisme interesting class ke labels hi nahi hain. Isolation Forest isliye kaam karta hai kyunki anomalies random splits se alag karna aasan hota hai. Method jo bhi ho, mushkil hissa threshold hai: zyada sensitive rakho to alerts koi padhta hi nahi.",
        "remember": "Threshold ko is hisaab se tune karo ki ek insaan roz kitne alerts sach me review kar sakta hai.",
        "mistake": "Contamination ka andaaza laga kar set karna aur on-call rota ko false alarms me duba dena.",
    },
    "voting classifier": {
        "plain": "Ensembles tab kaam karte hain jab members **alag** galtiyan karte hain. Correlated models ka average kuch nahi deta. Stacking meta-model ko out-of-fold predictions par train karta hai — in-fold predictions leak karte hain aur aisa meta-model dete hain jo perfect dikhta hai aur turant fail hota hai.",
        "remember": "Stacking sirf out-of-fold predictions par karo. In-fold predictions bhes badle hue leak hain.",
        "mistake": "0.2% faayde ke liye paanch-model ensemble ship karna aur inference cost aur failure modes paanch guna kar dena.",
    },
    "survival": {
        "plain": "Survival analysis 'event hone me kitna waqt' ka jawab deta hai jab kuch subjects ke saath ab tak hua hi nahi — wahi censoring hai, aur un rows ko phenk dena sab kuch bias kar deta hai. Churn, machine failure aur time-to-conversion sab survival problems hain jinhe log aam taur par classification samajh lete hain.",
        "remember": "Censored row bhi information rakhti hai: wo kam se kam itna to chali. Use kabhi drop mat karo.",
        "mistake": "Churn ko '30 din me churn hua haan/na' bana kar chupchap un sab ko hata dena jo pichhle hafte hi jude the.",
    },
    "causal": {
        "plain": "Prediction poochti hai 'kya hoga'; causal inference poochti hai 'agar main dakhal doon to kya hoga'. Model ek confounded correlation se perfectly predict kar sakta hai aur aapko ye salaah de sakta hai ki kya badalna hai — bilkul galat. Randomised experiments causal sawaalon ka jawab dete hain; observational data ko strong assumptions chahiye jo aapko likhni padengi.",
        "remember": "Kisi bhi observational effect ka matlab nikalne se pehle confounders ka naam lo. Naam na le sako to causality ka daawa mat karo.",
        "mistake": "Business ko X badalne ko kehna kyunki model ne X ko high feature importance di.",
    },
    "named entity recognition": {
        "plain": "Har cheez ko model nahi chahiye. Achhe format wale IDs, dates aur codes ke liye regex aur gazetteer aaj bhi fine-tuned model se behtar hain — zero latency aur poori explainability ke saath. BM25 keyword search abhi bhi strong retrieval baseline hai aur hybrid search isi ko embeddings ke saath jodta hai.",
        "remember": "Pehle regex try karo. Agar wo bina infrastructure ke 95% de deta hai, to model ko use replace karne ki wajah deni padegi.",
        "mistake": "Dates nikaalne ke liye transformer fine-tune karna jinhe `dateutil` pehle se sahi parse kar leta hai.",
    },
    "images as arrays": {
        "plain": "Image (height, width, channels) shape ka array hai jiski values 0-255 ya 0-1 hoti hain. Baaki sab — filters, edges, resizing — usi array par arithmetic hai. Classical CV aaj bhi tab jeetta hai jab scene controlled ho: fixed camera, fixed lighting, known object.",
        "remember": "Har model call se pehle channel order (RGB vs BGR) aur value range (0-255 vs 0-1) check karo.",
        "mistake": "OpenCV ka BGR aise model me daalna jo RGB par train hua tha, aur bina kisi dikhne wali wajah ke accuracy khona.",
    },
    "overfit a single batch": {
        "plain": "Debug ek tay kram me karo, sabse sasta test pehle. Kya model 20 rows par zero loss tak overfit kar sakta hai? Nahi, to bug data ya wiring me hai, capacity me nahi. Kya step zero par loss wahi hai jo random guessing se aana chahiye? Nahi, to labels ya output layer galat hai.",
        "remember": "Initialisation par expected cross-entropy ln(n_classes) hoti hai. Alag value matlab wiring bug.",
        "mistake": "Do din hyperparameters tune karna aise pipeline par jiske labels ek row se shift the.",
    },
    "aggregate metrics hide": {
        "plain": "Ek accuracy number aapko ye nahi batata ki kya theek karna hai. Galat predictions nikaalo, pachaas haath se padho, aur unhe buckets me baanto. Aam taur par ek bucket 40% errors ka hota hai aur uska fix obvious hota hai — aur hairaani ki baat ye ki achha khaasa hissa galat labels nikalta hai, galat predictions nahi.",
        "remember": "Error buckets ko total errors ke share se rank karo, error rate se nahi — wahi theek karo jo sach me mehnga pad raha hai.",
        "mistake": "Overall accuracy optimise karte rehna jab ek segment chupchap 0% de raha ho aur saari shikaayatein wahi se aa rahi hon.",
    },
    "what deep nets buy you": {
        "plain": "Deep learning tab apni keemat kamata hai jab raw inputs me aisi structure ho jise insaan haath se feature nahi bana sakta: pixels, audio, text. 50-column business table par gradient boosting aam taur par bahut kam mehnat me jeet jaata hai. Universal approximation kehta hai ki kaafi bada net us function ko *represent kar sakta hai* — ye nahi kehta ki aapka data aur optimiser use dhoondh lenge.",
        "remember": "Zyadatar projects me capacity bottleneck nahi hoti — data quality aur framing hoti hai.",
        "mistake": "3,000 tabular rows par neural network uthana aur ek line me bane random forest se haar jaana.",
    },
    "logits vs probabilities": {
        "plain": "Loss hi wo ek cheez hai jise model sach me optimise karta hai — baaki sab sajावat hai. Cross-entropy implementations ko logits do (probabilities nahi) jab wo logits maangti hain. Agar ek false negative false positive se das guna mehnga hai, to use loss ya threshold me likho, slide me nahi.",
        "remember": "Har error type ki asli keemat loss ya threshold me daalo — model use khud andaaza nahi laga sakta.",
        "mistake": "Fraud model ke liye saadi accuracy optimise karna jahan ek chook 10,000x false alarm ke barabar hai.",
    },
    "knowledge distillation": {
        "plain": "Training cost ek baar lagti hai; inference cost har request par hamesha ke liye. Distillation chhote student ko bade teacher ke outputs par train karta hai, quantisation weights ko kam bits me rakhta hai, aur ONNX ek artefact deta hai jo kai runtimes par chalta hai. Jitni accuracy jaa rahi hai use utni latency ke faayde ke saath naapo.",
        "remember": "Quantise karo, apne khud ke eval set par quality naapo, phir decide karo. Published benchmarks aapka task nahi hain.",
        "mistake": "int4 model isliye ship kar dena ki wo fit ho gaya, bina kabhi naape ki usne kitni accuracy li.",
    },
    "memory bandwidth": {
        "plain": "Zyadatar training runs compute-bound nahi hote; wo data ka intezaar kar rahe hote hain. Bada GPU khareedne se pehle utilisation dekho: agar wo 30% par baitha hai to fix aur data-loader workers ya tez storage format hai. Shuru karne se pehle cost ka andaaza lagao — ghante x instance price aisa number hai jise aap approve ya reject kar sakte ho.",
        "remember": "Scale karne se pehle profile karo. Dheema `__getitem__` chhote GPU se zyada paisa barbaad karta hai.",
        "mistake": "Chaar GPUs kiraye par lena aise bottleneck ke liye jo asal me single-threaded JPEG decode tha.",
    },
    "face detection vs recognition": {
        "plain": "Face technology technically aam hai aur legally aur ethically bhaari. Detection (chehra hai ya nahi) recognition (kiska chehra) se kahin kam sensitive hai. Kai jagah biometric processing par seedhi rok hai. Poochho ki kya koi non-biometric signal — badge scan, session token — wahi business sawaal hal kar deta hai.",
        "remember": "Biometric data aam taur par revoke nahi ho sakta. Use apni sabse sensitive category maano.",
        "mistake": "Face recognition isliye banana ki API aasan tha, bina lawful basis aur bina retention policy ke.",
    },
    "video as a sequence of frames": {
        "plain": "Video matlab frames plus time. Zyadatar practical systems ek second me kuch frames lete hain, har ek ko image model se embed karte hain, aur upar ek chhota temporal model lagate hain — 3D convolutions se kahin sasta. Tracking frames ke aar-paar detections ko jodti hai taaki '90 baar dikhi ek car' 90 cars na ban jaaye.",
        "remember": "Frames ko us sabse kam rate par sample karo jo sawaal ka jawab de de — video me yahi sabse bada cost lever hai.",
        "mistake": "30fps footage ka har frame process karna jab 2fps se wahi jawab 1/15 cost me mil jaata.",
    },
    "learning without labels": {
        "plain": "Self-supervised learning data se hi ek task gadh leta hai — ek image ke do augmented views match karo, ya masked patches wapas banao — taaki aap bina labels wale data par pretrain kar sako. Ye tab faayda deta hai jab aapke paas laakhon unlabelled samples hon aur labels kam, warna ye mehnga hai.",
        "remember": "Augmentations hi supervision hain — wahi tay karte hain ki model kis cheez ko bemaani maanega.",
        "mistake": "Hafton self-supervised pretraining karna jab ek public pretrained backbone pehle se behtar tha.",
    },
    "text detection vs text recognition": {
        "plain": "Document AI ek pipeline hai, model nahi: pehle dekho ki PDF me text layer hai ya nahi, na ho tabhi OCR karo, reading order aur layout wapas nikaalo, phir schema ke against fields extract karo. Aakhir me validation rules (kya total lines ke sum ke barabar hai?) behtar OCR model se zyada errors pakadte hain.",
        "remember": "Extracted fields par arithmetic aur schema checks wo OCR errors pakadte hain jinhe koi confidence score flag nahi karta.",
        "mistake": "Un PDFs par OCR chalana jinme pehle se perfect text layer tha, jisse cost badhi aur errors aaye.",
    },
    "onnx runtime": {
        "plain": "Device par aap accuracy ke badle latency, memory aur battery lete ho. Portable runtime me export karo, quantise karo, aur asli hardware par naapo — desktop benchmarks thermal load ke neeche phone ke baare me lagbhag kuch nahi batate.",
        "remember": "Target device par naapo, garam aur load ke neeche — apne laptop par, ek baar, thanda nahi.",
        "mistake": "Latency desktop GPU par validate karna aur pata chalna ki phone 40 second baad throttle kar deta hai.",
    },
    "depth from stereo": {
        "plain": "3D data depth maps, point clouds ya meshes me aata hai. Point clouds unordered sets hain, isliye models ko permutation-invariant hona padta hai (PointNet ka poora idea yahi hai). NeRF aur Gaussian splatting bahut saari photos se scene wapas banate hain aur compute-bhookhe par shaandaar hain.",
        "remember": "Stereo depth ki error doori ke square se badhti hai — door ki cheezein mushkil se naapi ja sakti hain.",
        "mistake": "Point cloud aise model ko dena jo point order par depend karta hai, aur har run me alag jawab paana.",
    },
    "annotation strategy": {
        "plain": "System design document wo sawaal poochne par majboor karta hai jo projects ko der se maarte hain: data kahan se aayega, model unsure ho to kya hoga, review kaun karega, ek inference ki cost kya hai, aur service down hone par kya hoga. Ise pehli training run se pehle likho.",
        "remember": "Fallback path ko 100% traffic sambhalna hi chahiye. Nahi sambhal sakta to aapne single point of failure banaya hai.",
        "mistake": "Sirf happy path ke liye design karna aur raat 3 baje pata chalna ki low-confidence cases ka koi raasta hi nahi hai.",
    },
    "why models need tokens": {
        "plain": "Tokenisers zyadatar English par train hote hain, isliye wahi vaakya Hindi ya Tamil me teen se paanch guna zyada tokens le sakta hai — matlab zyada paisa, kam context aur kharab quality. Kuch bhi price ya size karne se pehle apne asli users ki bhasha ka token cost check karo.",
        "remember": "Per request tokens apne users ki asli bhasha me naapo, English me nahi.",
        "mistake": "English samples se context window aur budget tay karna, phir aisi script me launch karna jo 4x mehngi hai.",
    },
    "relative position encoding": {
        "plain": "Lamba context aur lambi attention ek cheez nahi hai. Models lambe prompt ki shuruaat aur ant ka bharosemand istemaal karte hain aur beech me dhundhle ho jaate hain. Instruction aur sabse zaroori evidence kinaaron par rakho, aur ye mat maano ki 200k window matlab 200k usable attention.",
        "remember": "Order maayne rakhta hai. Sabse achha evidence pehle aur aakhir me; beech me wahi jahan attention patli hoti hai.",
        "mistake": "100 retrieved chunks retrieval order me thoons dena aur maan lena ki model sabko barabar padhta hai.",
    },
    "autoregressive generation": {
        "plain": "Generation ek loop hai: distribution predict karo, token chuno, jodo, dohrao. Greedy deterministic aur repetitive hai; sampling variety wala aur risky. Stop sequences aur max_tokens aapke circuit breakers hain — inke bina ek loop tab tak chal sakta hai jab tak aapka budget khatm na ho jaaye.",
        "remember": "max_tokens aur stop sequences hamesha set karo. Yahi bug aur bill ke beech ka farq hai.",
        "mistake": "Retry loop par max_tokens unbounded chhod dena aur raat bhar me mahine ka budget jala dena.",
    },
    "extractive vs abstractive": {
        "plain": "Context window se badi documents ke liye tree me summarise karo: chunk karo, har ek ka summary banao, phir summaries ka summary. Har level par detail khoti hai, isliye jo cheezein bachni hi chahiye (numbers, naam, decisions) unhe prose ke saath structured extraction me alag rakho.",
        "remember": "Facts structurally extract karo aur prose alag se summarise karo — summarisation sabse pehle numbers khoti hai.",
        "mistake": "Summary ki quality ROUGE se aankna, jo word overlap ko inaam deta hai aur sach hone ki parwah nahi karta.",
    },
    "conversation state": {
        "plain": "Context memory nahi hai. Context wo hai jo is request me aata hai; memory wo hai jise aap jaan-boojh kar store aur retrieve karte ho. Schema explicitly design karo — kya store hoga, kaise expire hoga, conflicts kaise sulajhenge — warna aapko aisa assistant milega jo wo baat pooray vishwas se dohraata hai jo user ne pichhle mahine sudhar di thi.",
        "remember": "Correction ko overwrite karna chahiye, saath rehna nahi. Do ulti memories dono retrieve ho jaayengi.",
        "mistake": "Har kahi hui baat hamesha ke liye vector store me jod dena, jisse purani aur sudhri hui baatein retrieval par ladti hain.",
    },
    "self-consistency": {
        "plain": "Reasoning modes tokens ke badle accuracy dete hain. Wo multi-step problems par madad karte hain jinka jawab verify ho sakta hai, aur lookup ya formatting tasks par paisa barbaad karte hain. Self-consistency — kai jawab sample karke majority lena — jab jawab compare ho sakte hon to sasta accuracy boost hai.",
        "remember": "Reasoning trace koi sabooot nahi hai. Likha hua reasoning galat ho sakta hai jabki jawab sahi ho, aur ulta bhi.",
        "mistake": "Extended thinking globally chaalu kar dena aur un tasks par cost teen guna kar dena jinhe ek reasoning token ki bhi zaroorat nahi thi.",
    },
    "parametric vs retrieved": {
        "plain": "Model ke weights me duniya ka ek jama hua, lossy snapshot hai, uske cutoff tak. Jo bhi badalta hai — prices, policies, staff, inventory — wo database ya retrieval index me hona chahiye, weights me nahi. Ye lakeer saaf khinch do aur hallucination rate kaafi gir jaata hai.",
        "remember": "Agar koi fact kal badal sakta hai, to use retrieve karo. Agar nahi badal sakta, to weights use rakh sakte hain.",
        "mistake": "Prices ko model me fine-tune kar dena aur har price list update par poora job dobara chalana.",
    },
    "chat completion request": {
        "plain": "Model tak jaane wala koi bhi network call kabhi na kabhi timeout hoga, rate-limit hoga, ya kharab output dega. Production client ko timeouts, bounded retries with exponential backoff aur jitter, concurrency cap, aur per-request cost logging chahiye. Ek baar likho aur har jagah use karo.",
        "remember": "Jitter zaroori hai: uske bina har client ek hi pal me retry karta hai aur outage dobara bana deta hai.",
        "mistake": "400-class error par infinite retries, jo kabhi safal nahi hoga, aur API aur budget dono par hathoda chalta rehta hai.",
    },
    "what llms are good and bad at": {
        "plain": "Stochastic hisse ko sabse chhote possible dabbe me rakho. Deterministic code tay kare ki kya call karna hai, jo wapas aaye use validate kare, aur permissions lagu kare; model beech me bas dhundhla bhaasha wala kaam kare. Un dono ke beech ki har seemaa ek validation ki jagah hai.",
        "remember": "Model prastaav deta hai; aapka code faisla karta hai. Kisi action se pehle aakhri check model output kabhi na ho.",
        "mistake": "Model ke apne 'confidence: 0.98' field par aise bharosa karna jaise wo calibrated probability ho.",
    },
    "why a protocol for tools": {
        "plain": "Tool protocol standardise karta hai ki model capabilities kaise dhoondhta aur call karta hai, taaki ek integration kai clients par chale. Asli sawaal security ka hai: third-party server wo sab dekhta hai jo aap bhejte ho aur aisa text laut sakta hai jo aapke agent ko steer kare. Ise aise review karo jaise network aur disk access wali dependency.",
        "remember": "Tool server ka response aapke agent ke liye untrusted input hai. Use delimit karo aur usse kabhi permissions mat dilwao.",
        "mistake": "Ek suvidha wala community server chaudi credentials ke saath install kar dena, bina jaanche ki wo upar kya bhej raha hai.",
    },
    "token economics": {
        "plain": "Cost per token galat metric hai; cost per resolved task sahi hai. Sasta model jo aadhi baar fail hokar escalate karta hai, mehnge model se zyada mehnga padta hai. Difficulty ke hisaab se route karo, aggressively cache karo, aur end-to-end naapo.",
        "remember": "Failure path ki keemat hamesha jodo. Human escalation aam taur par table ke har model cost par bhaari padta hai.",
        "mistake": "Sabse saste model par jaana, token spend girta dekhna, aur kabhi na notice karna ki support load double ho gaya.",
    },
    "capturing user feedback": {
        "plain": "Jin examples par aapka model galat hota hai wo aapke sabse keemti training data hain, aur wo muft hain — agar aap unhe capture karo. Pehle din se inputs, outputs aur corrections log karo; launch ke baad feedback loop lagane ka matlab hai zero se shuru karna.",
        "remember": "Sirf thumbs-down nahi, correction capture karo. 'Isse kya kehna chahiye tha' hi training signal hai.",
        "mistake": "Bina logging ke ship karna, phir teen mahine traffic ke baad sudhaarne ke liye koi data hi na hona.",
    },
    "code as a modality": {
        "plain": "Code me wo cheez hai jo text me nahi: ek oracle. Aap use chala sakte ho. Kisi bhi code-generating loop ko output compile, test aur lint karna chahiye aur failures wapas feed karni chahiye — yahi ek loop zyadatar quality gap band kar deta hai. Generated code ko asli credentials ke saath chalne se pehle injected dependencies aur unsafe calls ke liye review karo.",
        "remember": "Test failure ka text seedha context me wapas do — wo aapke paas ka sabse high-signal prompt hai.",
        "mistake": "Aisa generated code accept kar lena jo aisa package import karta hai jiska astitva kisi ne verify nahi kiya (asli supply-chain vector).",
    },
    "open weights vs open source": {
        "plain": "'Open weights' matlab 'open source' nahi — kai licences commercial use, scale ya redistribution par rok lagate hain. Self-hosting tab sahi hai jab data residency, oonchi steady volume, ya bhaari customisation ho; APIs spiky traffic aur zero ops par jeette hain. Ideology se pehle ganit karo.",
        "remember": "Self-hosting ki cost tab bhi chalti hai jab traffic nahi chalta. Spiky workloads lagbhag hamesha API ke haq me hote hain.",
        "mistake": "24/7 GPU kiraye par lena aise workload ke liye jo din me do ghante 8% utilisation par peak karta hai.",
    },
    "data schema test": {
        "plain": "ML tests parton me aate hain: transforms par unit tests, data par contract tests, behaviour par metamorphic tests (bemaani feature jodne se prediction nahi badalni chahiye), aur fixture dataset par chhota end-to-end run. Poora suite ek minute ke andar rakho warna koi use chalayega hi nahi.",
        "remember": "Randomness chhoone wale har test ko explicit seed milna chahiye. Parallelism ke neeche global seeding kaafi nahi hai.",
        "mistake": "Itna dheema test suite ki CI use skip kar de aur bugs phir bhi production tak pahuch jaayein.",
    },
    "feature store": {
        "plain": "Training/serving skew tab hota hai jab offline nikala gaya feature request time wale se alag ho — alag code, alag window, alag timezone. Feature store ise ek baar compute karke dono raaston ko serve karke theek karta hai. Zyadatar teams ke liye ek shared function plus tests hi kaafi hai.",
        "remember": "Ek function, dono raaston me import kiya gaya, ek test ke saath jo sabit kare ki dono barabar hain. Feature store ka 90% yahi hai.",
        "mistake": "Training me SQL feature aur serving me haath se likha Python reimplementation, jo chupchap alag ho jaate hain.",
    },
    "batch vs streaming ingestion": {
        "plain": "Pipelines idempotent honi chahiye: wahi din dobara chalane par wahi result aaye, duplicates nahi. Output ko date se partition karo taaki backfill poori table ke bajaye ek partition dobara likhe. Pehle batch — streaming operational cost double kar deta hai aur zyadatar teams ko wo latency chahiye hi nahi.",
        "remember": "Idempotent + partitioned = safe backfills. Append-only pipelines har rerun ko data corruption bana deti hain.",
        "mistake": "Aisi pipeline jo append karti hai, jisse retry hua job chupchap kal ke numbers double kar deta hai.",
    },
    "roles: research": {
        "plain": "ML estimates isliye bharosemand nahi hote kyunki jab tak aap dekh na lo, aapko pata hi nahi hota ki signal hai bhi ya nahi. Phases me estimate do, kill criteria ke saath: 'do hafte ye dekhne ke liye ki baseline rule ko haraata hai; nahi to hum ruk jaayenge'. Stakeholders uncertainty ko chhooti hui deadline se kahin behtar sweekar karte hain.",
        "remember": "Ranges aur kill criteria do, kabhi bhi aise kaam ki ek fix date nahi jiski feasibility hi unknown hai.",
        "mistake": "Planning meeting me 95% accuracy ka vaada karna, is se pehle ki kisi ne data dekha bhi ho.",
    },
    "structure of a good technical write-up": {
        "plain": "Pehle result, phir method, phir caveats. Zyadatar padhne wale do paragraph ke baad ruk jaate hain, isliye pehle do me finding aur uski ahmiyat honi chahiye. Aisa README jo problem, number aur chalane ka tarika batata ho, kisi perfect architecture diagram se zyada keemti hai.",
        "remember": "Number pehle paragraph me daalo. Agar aap use chhupa rahe ho to padhne wala maan lega ki wo bura hai.",
        "mistake": "Aisa README jo 400 lines me architecture samjhaata hai aur kabhi nahi batata ki score kya aaya.",
    },
    "where papers appear": {
        "plain": "Teen pass me padho: title/abstract/figures (5 minute, tay karo ki matlab hai ya nahi), method aur results (30 minute, idea samjho), phir poori detail sirf tab jab aap implement karoge. Limitations section aam taur par paper ka sabse imaandaar paragraph hota hai — use jaldi padho.",
        "remember": "Dekho unhone kin baselines se compare kiya. Kamzor baseline har method ko strong dikha deta hai.",
        "mistake": "Bees papers padhna aur ek bhi implement na karna — bina banaye samajh ek hafte me udd jaati hai.",
    },
    "ai engineer and the llm application role": {
        "plain": "Roles algorithms me kam, aur is baat me zyada alag hain ki din kahan jaata hai: research experiments par, ML engineering pipelines aur serving par, AI engineering prompts, retrieval aur evals par, data engineering us plumbing par jis par baaki sab tika hai. Wo din chuno jo aap jeena chahte ho, wo title nahi jo achha lagta ho.",
        "remember": "Ek project jise aap end-to-end defend kar sako, aapke CV par das tutorials se bhaari hai.",
        "mistake": "Sabse oonchi salary wale title ke peeche bhaag kar aisa kaam lena jo aapko har roz uba deta hai.",
    },
    "weekly learning cadence": {
        "plain": "Tutorial hell matlab dekhna, banana nahi. Ilaaj ek cadence hai: thoda padho, kuch chhota banao jo fail ho sakta ho, aur likho ki kya chaunkane wala tha. Kisi aur ko concept samjhana sabse tez test hai ki aapko sach me samajh aaya ya nahi.",
        "remember": "Agar aap bina notes ke samjha nahi sakte, to aapne seekha nahi — sirf dekha hai.",
        "mistake": "Dasva course poora karna jabki aapne aisa kuch ship nahi kiya jise koi aur chala sake.",
    },
    "what 200 days actually gave you": {
        "plain": "Is course ke frameworks badal jaayenge; fundamentals nahi. Linear algebra, probability, imaandaar evaluation, leakage, aur ye jaanna ki aapka data kya support kar sakta hai aur kya nahi — ye har library se zyada jeeyenge. Khud ka audit inhi ke against karo, tool list ke against nahi.",
        "remember": "Ant me Day 1 wale gyaan se ek project dobara banao. Dono versions ka farq hi aapki pragati hai.",
        "mistake": "Apni kaabiliyat un tools ki ginti se naapna jinhe aapne chhua, un problems se nahi jinhe aapne hal kiya.",
    },
}


def teach_hi(concept: str, theme: str = "") -> dict[str, str]:
    """Hinglish prose for a concept, with the English code sample.

    Falls back to English prose for any BANK entry not yet translated, and to
    a Hinglish generic lesson when the concept matches no bank entry at all.
    """
    en = teach(concept, theme)
    for entry in BANK:
        if entry["code"] != en["code"]:
            continue
        hi = HI.get(entry["keys"][0])
        if hi:
            return {"plain": hi["plain"], "code": en["code"],
                    "remember": hi["remember"], "mistake": hi["mistake"]}
        return en          # matched the bank, prose not translated yet
    return {
        "plain": (
            f"Aaj ka idea — **{concept}** — {theme or 'applied AI'} ke theme ke andar aata hai. "
            "Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya "
            "maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?"
        ),
        "code": en["code"],
        "remember": f"`{concept}` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.",
        "mistake": f"`{concept}` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.",
    }


def _self_check() -> None:
    first_keys = {e["keys"][0] for e in BANK}
    unknown = set(HI) - first_keys
    assert not unknown, f"HI keys not present in BANK: {sorted(unknown)}"
    hit = teach_hi("Broadcasting rules", "NumPy foundations")
    assert "NumPy" in hit["plain"] and "rakhta hai" in hit["plain"], hit["plain"]
    miss = teach_hi("Some entirely unmatched concept xyzzy", "nothing")
    assert "xyzzy" in miss["remember"]
    print(f"teach_hi.py ok — {len(HI)}/{len(BANK)} bank entries translated "
          f"({100 * len(HI) / len(BANK):.0f}%)")


if __name__ == "__main__":
    _self_check()
