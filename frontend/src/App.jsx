import React from 'react';

import SearchBar from './components/SearchBar';

const App = () => {

  return (
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column', justifyContent: 'center'}}> 
        <SearchBar></SearchBar>
    </div>
  )
}

export default App;