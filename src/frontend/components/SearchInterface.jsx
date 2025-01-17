
    import React, { useState } from 'react';
    import axios from 'axios';

    const SearchInterface = () => {
      const [query, setQuery] = useState('');
      const [results, setResults] = useState([]);
      const [loading, setLoading] = useState(false);

      const handleSearch = async () => {
        setLoading(true);
        try {
          const response = await axios.post('/api/search', { query });
          setResults(response.data);
        } catch (error) {
          console.error('Search error:', error);
        }
        setLoading(false);
      };

      return (
        <div className="search-interface">
          <div className="search-bar">
            <input
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search..."
            />
           