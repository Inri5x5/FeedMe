import React from 'react'
import styles from './styles/SelectedIngredientLabel.module.css'

const SelectedIngredientLabel = (props) => {
  return (
    <div className={styles.tag}> 
        <span className={styles.tag_title}> {props.object.name} </span>
        <span className={styles.tag_close_icon} onClick={() => props.removeIngredient(props.object)}> x </span>
    </div>
  )
}

export default SelectedIngredientLabel