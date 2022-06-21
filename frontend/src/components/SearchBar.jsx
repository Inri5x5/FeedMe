import React from 'react'
import { useEffect, useState, useRef } from 'react';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import styles from './styles/SearchBar.module.css'
import SearchIcon from '@mui/icons-material/Search';

const SearchBar = () => {
  const [showDropdown, setDropdown] = useState(false);
  const myDropdown = useRef(null);
  const clickDropdown = () => {
    if (!showDropdown === false) {
      myDropdown.current.blur();
    }
    setDropdown(!showDropdown);
  }
    
  return (
    <div className={styles.search_bar}>
        <div className={styles.search_category} tabIndex='0' ref={myDropdown} onClick={() => {clickDropdown()}} onBlur={() => setDropdown(false)}>
            <div className={styles.search_category_link}>
                <span>Categories</span>
                <KeyboardArrowDownIcon className={styles.search_category_icon}/>
            </div>
            <div className={styles.category_menu} >
                <a href="#" className={styles.category_menu_item}>Lorem</a>
                <a href="#" className={styles.category_menu_item}>Lorem</a>
                <a href="#" className={styles.category_menu_item}>Lorem</a>
                <a href="#" className={styles.category_menu_item}>Lorem</a>
                <a href="#" className={styles.category_menu_item}>Lorem</a>
            </div>
        </div>
        <div className={styles.input_search}>
            <input type="text" placeholder="Search Your Ingredient" />
            <div className={styles.search_menu}>
                <div className={styles.search_related}>
                    <a href="#">
                        <span>Lorem</span>
                    </a>
                    <a href="#">
                        <span>Lorem</span>
                    </a>
                </div>
            </div>
        </div>
        <a href="#" className={styles.search_btn}>
            <SearchIcon className={styles.search_btn_icon}></SearchIcon>
        </a>
    </div>
  

  )
}

export default SearchBar