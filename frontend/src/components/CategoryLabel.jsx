import React from 'react'
import styles from './styles/CategoryLabel.module.css'

const CategoryLabel = (props) => {
  return (
    <div className={styles.tag} onClick={() => {props.setMenuName(props.text); props.setDropdownState()}}> 
        <span className={styles.tag_title}> {props.text} </span>
    </div>
  )
}

export default CategoryLabel