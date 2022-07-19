 import React from 'react'
import styles from './styles/IngredientLabel.module.css'

const IngredientLabel = (props) => {
  return (
    <div className={props.isSelected ? styles.tag_selected : styles.tag } onClick={() => props.clickFunction(props.object)}> 
        <span className={styles.tag_title}> {props.object.name} </span>
    </div>
  )
}

export default IngredientLabel