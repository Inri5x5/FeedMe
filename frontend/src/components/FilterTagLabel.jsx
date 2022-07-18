import React from 'react'
import styles from './styles/FilterTagLabel.module.css'

const FilterTagLabel = (props) => {
    return (
      <div className={styles.tag}> 
          <span className={styles.tag_title}> {props.name}</span>
      </div>
    )
}

export default FilterTagLabel;