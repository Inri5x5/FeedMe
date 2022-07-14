import React from 'react'
import styles from './styles/SelectedTagLabel.module.css'

const SelectedTagLabel = (props) => {
  return (
    <div className={(props.object.tag_name === '+') ? styles.add_tag : styles.tag}> 
        <span className={styles.tag_title}> {props.object.tag_name} </span>
        {(props.object.tag_name !== '+') && <span className={styles.tag_close_icon} onClick={() => props.clickFunction(props.object)}> x </span>}
    </div>
  )
}

export default SelectedTagLabel