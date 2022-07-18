import React from 'react'
import styles from './styles/TagLabel.module.css'

const TagLabel = (props) => {
  let style;
  
  if (props.object.name === '+') {
    style = styles.add_tag
  } else if (props.isSelected) {
    style = styles.tag_focus
  } else {
    style = styles.tag
  }

  return (
    <div className={style} onClick={() => {(props.object.name === '+') ? props.clickFunction() : props.clickFunction(props.object)}}> 
        <span className={styles.tag_title}> {props.object.name} </span>
    </div>
  )
}

export default TagLabel