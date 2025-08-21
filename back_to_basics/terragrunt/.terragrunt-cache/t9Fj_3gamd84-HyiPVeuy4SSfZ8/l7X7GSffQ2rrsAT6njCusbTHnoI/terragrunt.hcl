terraform {
  source = "../shared"
}

dependency "foo" {
  config_path = "../foo"
  mock_outputs = {
    content = "Mocked content from foo"
  }
}

inputs = {
    output_dir = get_terragrunt_dir()
    content = "Foo content: ${dependency.foo.outputs.content}"
}