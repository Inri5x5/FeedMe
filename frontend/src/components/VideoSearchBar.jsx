import React, { useState } from "react";
import SearchIcon from '@mui/icons-material/Search';
import CloseIcon from '@mui/icons-material/Close';
import styles from './styles/VideoSearchBar.module.css'

function VideoSearchBar(props) {

  const placeholder = "Search for some video"

  const handleFilter = (event) => {
    const searchWord = event.target.value;
    props.setWordEntered(searchWord);
  };

  const clearInput = () => {
    props.setWordEntered("");
  };

  return (
    <div className={styles.search}>
      <div className={styles.searchInputs}>
        <input
          className={styles.search_input}
          type="text"
          placeholder={placeholder}
          value={props.wordEntered}
          onChange={handleFilter}
        />
        <div className={styles.searchIcon}>
          {props.wordEntered === "" ? (
            <SearchIcon />
          ) : (
            <CloseIcon onClick={clearInput} />
          )}
        </div>
      </div>
    </div>
  );
}

export default VideoSearchBar;