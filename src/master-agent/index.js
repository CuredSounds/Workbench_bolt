const express = require('express');
    const axios = require('axios');
    const app = express();
    const port = 3000;

    const AGENT_ENDPOINTS = {
      SCRAPER: 'http://localhost:3001/scrape'
    };

    app.use(express.json());

    app.post('/delegate-task', async (req, res) => {
      const { taskType, parameters } = req.body;
      
      try {
        let result;
        switch (taskType) {
          case 'SCRAPE':
            result = await axios.post(AGENT_ENDPOINTS.SCRAPER, parameters);
            break;
          default:
            return res.status(400).json({ error: 'Invalid task type' });
        }
        
        res.json({
          status: 'Task completed',
          taskType,
          result: result.data
        });
      } catch (error) {
        console.error('Task delegation error:', error);
        res.status(500).json({ error: 'Task execution failed' });
      }
    });

    app.listen(port, () => {
      console.log(`Master Agent running on port ${port}`);
    });
