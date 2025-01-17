const { pipeline } = require('@xenova/transformers');

    class AIProcessor {
      constructor() {
        this.models = {};
      }

      async initialize() {
        this.models.summarizer = await pipeline('summarization');
        this.models.sentiment = await pipeline('sentiment-analysis');
        this.models.ner = await pipeline('ner');
      }

      async summarize(text, options = {}) {
        return this.models.summarizer(text, {
          max_length: options.maxLength || 130,
          min_length: options.minLength || 30,
          do_sample: false
        });
      }

      async analyzeSentiment(text) {
        return this.models.sentiment(text);
      }

      async extractEntities(text) {
        return this.models.ner(text);
      }
    }

    module.exports = AIProcessor;
