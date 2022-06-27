import React from 'react'
import styles from './styles/CategoryLabel.module.css'

const CategoryLabel = (props) => {
  return (
    <div className={styles.tag} onClick={() => {props.setMenuName(props.object); props.setDropdownState()}}> 
        <span className={styles.tag_title}> {props.object.name} </span>
    </div>
  )
}

export default CategoryLabel