/**
 * @fileoverview This module handles displaying various database resources in
 *   neat and orderly tables.
 * @author Alvin Lin (axl1439)
 */

const colors = require('colors')
const Table = require('cli-table3')

const json = () => {
  return process.argv.includes('--json')
}

exports.displaySales = sales => {
  if (json()) {
    console.log(sales)
  } else {
    const table = new Table({ head: ['ID', 'Customer ID', 'Dealer ID']})
    table.push(...[
      [1, 3, 11],
      [2, 3, 12],
      [3, 6, 33],
      [4, 3, 11],
      [5, 8, 33]
    ])
    console.log(table.toString())
  }
}

exports.displayDealers = dealers => {
  if (json()) {
    console.log(sales)
  } else {
    const table = new Table({
      head: ['ID', 'Name', 'Phone']
    })
    table.push(...[
      [1, 'Bob', '7183029439'],
      [2, 'John', '120309203'],
      [3, 'Dick', '1239234503'],
      [4, 'Richard', '123483904'],
      [5, 'Corn', '911'],
    ])
    console.log(table.toString())
  }
}
