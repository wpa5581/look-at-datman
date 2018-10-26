/**
 * @fileoverview Module handling the dealer subcommands.
 * @author Alvin Lin (axl1439)
 */

exports.command = 'brand'

exports.aliases = ['brands']

exports.description = 'Manage brands in the database'

exports.builder = yargs => {
  yargs.commandDir('brands').demandCommand()
}
