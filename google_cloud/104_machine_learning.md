### Machine Learning

#### Cloud ML Engine (Regional)
* Regional; ~ AWS Machine Learning.
* Based on TensorFlow.
* Integrates: GCS/BQ (storage)l Cloud Datalab(dev), Cloud Dataflow (preprocessing)
* Support online (low latency) or batch (job time).
* Can download triqaned model to desktop, mobile, private servers.
* `HyperTune`: automatically tybes model hyperparameters.

#### Cloud Vision API (Global)
* Classifies images to thousands of categories; pre-trained ML models.
* ~ AWS Rekognition.
* Pay per image based on task nature (faces, text, logo, landmarks).

#### Cloud Speech API (Global)
* Spoken words to text.
* 110 languages.
* Pre-recorded or real-time audio.
* Handle noisy source, slang, contextual hints.
* Pay per 15s of audio.

#### Cloud Natural Language API (Global)
* Sentiment, intent, content classification, syntax analysis (dependency trees)/
* Speech API (audio); Vision API (OCR); Translation API.
* Pay per 1000 characters.

#### Cloud Translation API (Global)
* Translation between 100+ languages. Auto-detect source languages.
* Can translate semantics, not just syntax.
* Pay per character processed for translation.

#### Diaglogflow (Global)
* Chatbox: conversational interfaces.
* ~ Amazon Lex.

#### Cloud Video Intelligence API (Regional, Global)
* Annotates videos. What are contained.
* Label: dog, flower, car.
* Shot change: scene changes in videos.
* Adult content.

#### Cloud Job Discovery (Global)
* Help job seekers search job seeking databases.
* Recognizing context, abbreviation, jargons.

#### Prediction API (Deprecated)
* RESTful API for training ML models.
* Shut down on Apr 2018.

#### Reference
* TensorFlow: https://www.tensorflow.org/
* Cloud Machine Learning: https://cloud.google.com/ml/
* Vision API: https://cloud.google.com/vision/
* Translate API: https://cloud.google.com/translate/
* Speech API: https://cloud.google.com/speech/
