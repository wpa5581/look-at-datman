/**
 * @fileoverview Module handling the customer subcommands.
 * @author Alvin Lin (axl1439)
 */

exports.command = 'customer'

exports.aliases = ['customers']

exports.description = 'Manage customers in the database'

exports.builder = yargs => {
  yargs.commandDir('customers').demandCommand()
}
