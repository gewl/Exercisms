//
//  Leap.swift
//  leap-swift
//
//  Created by gewl on 11/12/16.
//  Copyright © 2016 gewl. All rights reserved.
//

import Foundation

struct Year {
    let calendarYear: Int
    
    init(calendarYear: Int) {
        self.calendarYear = calendarYear
    }
    
    var isLeapYear = true
}
