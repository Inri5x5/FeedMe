import React from 'react'
import styles from './styles/SelectedTagLabel.module.css'

const SelectedTagLabel = (props) => {
  let style;
  if (props.object.name === '+') {
    style = styles.add_tag
  } else if (props.isExcluded) {
    style = styles.tag_excluded
  } else if (props.isIncluded) {
    style = styles.tag_included
  } else {
    style = styles.tag
  }
  return (
    <div className={style}> 
        <span className={styles.tag_title}> {props.object.name} </span>
        {(props.object.name !== '+') && <span className={styles.tag_close_icon} onClick={() => props.clickFunction(props.object)}> x </span>}
    </div>
  )
}

export default SelectedTagLabel